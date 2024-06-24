from model.model import Model
from sklearn.metrics import confusion_matrix
import pandas as pd

class Sentiment:
    """
    This class provides a handler for running a model on different datasets for sentiment analysis.
    """

    def __init__(self):
        """
        Initialize the Sentiment class with predefined datasets and their labels.
        
        The class contains a dictionary of datasets, each with a path to a CSV file and corresponding labels. 
        It also initializes variables to keep track of the currently loaded dataset (DataFrame) and its name.
        """

        self._datasets =    {   'sd-twitter': {'path': 'data/twitter.csv', 'labels': [['negative', '0'], ['positive', '1'], ['neutral', '2'], ['irrelevant', '3']]}, 
                                'sd-finance': {'path': 'data/finance.csv', 'labels': [['negative', '0'], ['positive', '1'], ['neutral', '2']]}, 
                                'sd-imdb': {'path': 'data/imdb.csv', 'labels': [['negative', '0', 'no'], ['positive', '1', 'yes']]}
                            }
        self._current_dataset = None
        self._current_dataset_name = None

    
    def _load(self, dataset: str):
        """
        Load the specified dataset if it's not already loaded.

        Args:
            dataset (str): The name of the dataset to load.

        Returns:
            bool: True if the dataset corresponds to a correct dataset name, False otherwise.
        """

        if self._current_dataset_name != dataset:
            if dataset in self._datasets:
                self._current_dataset_name = dataset
                self._current_dataset = pd.read_csv(self._datasets[dataset]['path'], header=None)

            else:
                return False

        return True

    def _assign_label(self, output: str, dataset: str):
        """
        Assign a label to the model's output based on the dataset's labels.

        Args:
            output (str): The model's output string.
            dataset (str): The name of the dataset.

        Returns:
            str: The assigned label or 'unlabeled' if no match is found.
        """

        output = output.lower() # Convert output to lowercase
        
        labels = self._datasets[dataset]['labels']  # Get the labels for the dataset

        found = False
        i = 0

        # Loop through the labels to find a match in the output
        while i < len(labels) and not found:
            j = 0

            while j < len(labels[i]) and not found:
                if labels[i][j] in output:
                    found = True

                j = j + 1
            
            if not found:
                i = i + 1

        # If no label is found, return 'unlabeled'
        if not found:
            return 'unlabeled'

        else:
            return labels[i][0]

    def run(self, dataset: str, model: Model, instances: int, left: str, right: str):
        """
        Run the sentiment analysis on the given dataset using the specified model.

        Args:
            dataset (str): The name of the dataset.
            model (Model): The model to use for prediction.
            instances (int): The number of instances to sample from the dataset (the same seed is always used).
            left (str): The left context string to prepend to each instance.
            right (str): The right context string to append to each instance.

        Returns:
            str: The accuracy of the model's predictions formatted as a string.
        """

        # Check if the dataset is loaded and the model is not None
        if self._load(dataset) and model:
            # Ensure at least one instance is processed and it doesn't exceed the dataset size
            instances = max(1, instances)
            instances = min(len(self._current_dataset), instances)
            
            results = []

            # Sample a subset of the dataset
            samples = self._current_dataset.sample(n=instances, random_state=42)

            for index, row in samples.iterrows():
                # Construct input text for the model
                inpt = left + ' ' + row[0] + ' ' + right

                # Run the model to get the output
                generated_out = model.run(inpt)
        
                # Assign a label to the model's output
                prediction = self._assign_label(generated_out, dataset)
                
                # Append the real and predicted labels to the results
                results.append({'real_label': row[1], 'pred_label': prediction})

            # Convert the results list to a DataFrame
            results = pd.DataFrame(results)

            # Calculate the accuracy
            accuracy = (results['real_label'] == results['pred_label']).mean()    
            
            # Labels for the confusion matrix
            labels = sorted(list(results['real_label'].unique()) + ['unlabeled'])

            # Calculate confusion matrix
            cm = confusion_matrix(results['real_label'], results['pred_label'], labels=labels)

            # Create DataFrame with confusion matrix
            cm_df = pd.DataFrame(cm, index=labels, columns=labels)

            return f'Accuracy: {accuracy:.3f}\n\nConfusion Matrix (True = rows, Predicted = columns):\n\n{cm_df}'

        else:
            return ''
