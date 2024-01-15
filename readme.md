# This repository contains all generalized code snippets and templates relating to model experimentation, training, evaluation, testing, server-side loading, client-side requests, usage documentation, loaders, evaluators, visualizers, and preprocessor utilities, and the model architectures, figures, and final folder

# requirements:
1. git
2. conda
3. python

# Source code usage
1. assuming git is installed clone repository by running `git clone https://github.com/08Aristodemus24/<repo name>`
2. assuming conda is also installed run `conda create -n <environment name e.g. some-environment-name> python=x.x.x`. Note python version should be `x.x.x` for the to be created conda environment to avoid dependency/package incompatibility.
3. run `conda activate <environment name used>` or `activate <environment name used>`.
4. run `conda list -e` to see list of installed packages. If pip is not yet installed run conda install pip, otherwise skip this step and move to step 5.
5. navigate to directory containing the `requirements.txt` file.
5. run `pip install -r requirements.txt` inside the directory containing the `requirements.txt` file
6. after installing packages/dependencies run `python index.py` while in this directory to run app locally

# App usage:
1. control panel of app will have 3 inputs: prompt, temperature, and sequence length. Prompt can be understood as the starting point in which our model will append certain words during generation for instance if the prompt given is "jordan" then model might generate "jordan is a country in the middle east" and so on. Temperature input can be understood as "how much the do you want the model to generate diverse sequences or words?" e.g. if a diversity of 2 (this is the max value for diversity/temperature by the way) then then the model might potentially generate incomprehensible words (almost made up words) e.g. "jordan djanna sounlava kianpo". And lastly Sequence Length is how long do you want the generated sequence to be in terms of character length for isntance if sequence length is 10 then generated sequence would be "jordan is."

# Articles
1. multiple/ensemble model training: 
* https://www.geeksforgeeks.org/lazy-predict-library-in-python-for-machine-learning/
* https://medium.com/omics-diary/how-to-use-the-lazy-predict-library-to-select-the-best-machine-learning-model-65378bf4568e

2. evaluating ensemble models:

# Pre-built template functions for projects:
~ - done
^ - needs further testing
& - needs further understanding
! - needs further tweaking

Loaders:
NLP
* load_corpus
* get_chars
* construct_embedding_dict
* construct_embedding_matrix

General
* load_lookup_array
* save_lookup_array
* load_meta_data
* save_meta_data
* get_cat_cols
* get_top_models
* load_model
* save_model
* create_metrics_df ~
* create_classified_df ~

Image Processing
* create_image_set

Preprocessors:
NLP
* map_value_to_index
* remove_contractions
* rem_non_alpha_num
* capitalize
* filter_valid
* partition_corpus
* rem_stop_words
* stem_corpus_words
* lemmatize_corpus_words
* string_list_to_list
* flatten_series_of_lists
* sentences_to_avgs
* init_sequences
* decode_id_sequences
* decode_one_hot ~

Recommendation
* normalize_ratings
* normalize_rating_matrix

General
* normalize_train_cross
* encode_features ~
* translate_labels ~

Visualizers:
* plot_train_cross_features ~
* analyze ~ 
* view_words
* data_split_metric_values ~
* view_value_frequency ! has no x label
* multi_class_heatmap ~
* view_metric_values ~
* view_classified_labels ~
* view_label_freq ! has no x label
* disp_cat_feat ! has x labels but bars are too compressed especially if n unique is large
* describe_col
* visualize_graph
* plot_evolution ~
* view_clusters_3d ~
* ModelResults ! since there might be a shorter version of code for it from the micro-organism-classifier kaggle code
* plot_all_vars ~

# Prebuilt template components for client-side:
* WE NEED TO IMPLEMENT NOW THESE TEMPLATES FOR OUR MICRO-ORGANISM-CLASSIFIER
* <s>submit button ~</s>
* <s>100vh section for landing page ~</s>
* <s>text input fields ~</s>
* <s>range input fields ~</s>
* <s>number input fields ~</s>
* <s>file input fields ~</s>
* <s>select fields ~</s>
* <s>textarea fields ~</s>
* <s>fix width of data-form-content why does it not expand the width of the parent? ~ it was because of its parent data-form-section being set to display flex and shrinking it to the width of childrens size, or in other words in auto</s>
* <s>fix image upload field spacing ~</s>
* <s>fix image upload fields upload button ~</s>
* <s>create custom themed classes to switch between themes for components</s>
* <s>implement dark</s>
* <s>tweak light shadow of light theme</s>
* fix image upload fields image height ! needs to be responsive from 1600px to 320px

# Prebuilt template functions for server-side
* for general models
* for tensorflow models
* using a pipeline for preprocessing user input from client-side using 
a preprocessing function e.g. featture vector -> normalizer loaded with 
specific mean and standard deviation, do I use a saved .json object with
these hyper params, or use a sklearn object instead? But a sklearn object 
like a normalizer I cannot save

```
def predict(self, X):
        # normalize on training mean and standard dev first
        X = (X - self.mean) / self.std_dev

        # predict then return prediction value
        return self.linear(X)
```

<s>use instead your own implementation of a normalizer function and then loading
the respective hyper params like mean and standard deviation to pass into 
this from scratch implementation of a normalizer</s>

<s>but not only for an a normalizer, what about for OrdinalEncoder() and 
LabelEncoder() objects? I really can't save them because it would just be too much</s>

<s>if there is a dataset X and it has categorical variables
does we really need to save the encoder we used on this dataset to use on the</s>

X_train
yes, bacteria
no, archaea
no, eukarya
yes, eukarya
no, bacteria

X_cross
no, bacteria
yes, eukarya

<s>AH YES. we really need to save the encoder or find some way to use the encoders
information that was obtained from the whole dataset (since we do
not split the data set if we encode the features because potential categories
of features may be lost on splitting the data) because if we use a new encoder 
on the cross dataset the features may be such that some would be missing that 
would exist in the train data, e.g. bacteria and archaea are the only features 
so we don't want to encode it as only 0 and 1 since and in the whole data there 
are 3 categories for a feature nsmrly bacteria, archaea, and eukarya which are 
encoded to 0</s>

**or just save the sklearn encoders as well** using save_model() and load it using load_model()


* <s>there needs to be also a meta_data saver like this
```
def save_weights(self):
    meta_data = {
        'non-bias': self.theta.tolist(),
        'bias': self.beta.tolist()[0],
        'mean': self.mean.tolist(),
        'std_dev': self.std_dev.tolist()
    }

    # if directory weights does not already exist create 
    # directory and save weights there
    if os.path.exists('./weights') != True:
        os.mkdir('./weights')
    
    with open('./weights/meta_data.json', 'w') as out_file:
        json.dump(meta_data, out_file)
        out_file.close()
```
</s>

for both general and deep learning models. But since sklearn models can be saved directly without taking into account its hyperparams, we could only now save certain other hyperparams like again mean and standard deviation

or in tensorflow models some meta_data may be important to load later on such as:
```
# global variables
vocab = None
char_to_idx = None
idx_to_char = None
hyper_params = None
```
just in case a model only saves its weights, and not the whole model architecture such as hyper_params in this case

but even if the architecture itself is saved its respective hyper params, for preprocessing input in order to feed to the trained model it is important that such hyperparams used in preprocessing the input for having even trained the model in the first place is important, this being vocab, char_to_idx, and idx_to_char for instance

* writing decoders functions for the predictions of our model
- decoder for categorical data which can range from:
a. categorical vectors to image class
b. categorical sequences of vectors to sentences
c. categorical vectors to sentiments/emotional reactions class (such is the case for NLP)

* write preprocessor for when user inputs an image from the client-side
* writing dropout for CNNs https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/

