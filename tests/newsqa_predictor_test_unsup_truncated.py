import torch 
from data_loaders.language_model_loader_truncate import LanguageModelLoaderTruncate
from models.language_model import LanguageModel
from models.language_trainer import LanguageTrainer
from models.language_wrapper import LanguageWrapper 
from helpers import constants 
from helpers import torch_utils, utils
from torch.autograd import variable

dataset_path = 'datasets/newsqa_unsupervised_verb_filtered'
load_path = 'logs/squad_saved_data_truncated/model_14.pyt7' # CHANGE THIS TO EHATEVER YOU WANT

language_model_loader = LanguageModelLoaderTruncate(dataset_path, tokenizer_type=constants.TOKENIZER_TAB)
language_model = torch_utils.load_model(load_path).cuda()
language_model.config['save_directory'] = 'logs/newsqa_saved_data'

language_wrapper = LanguageWrapper(language_model, language_model_loader.get_vocab())
language_trainer = LanguageTrainer(language_model.config, language_wrapper, language_model_loader)

#test_predictions = language_trainer.predict(dataset_type=constants.DATASET_TEST,
#            epoch_num=10, max_length=20)
#dev_predictions = language_trainer.predict(dataset_type=constants.DATASET_VALIDATION, 
#            epoch_num=10, max_length=10)
train_predictions = language_trainer.predict(dataset_type=constants.DATASET_TRAIN, 
            epoch_num=10, max_length=10)

utils.save_lines(train_predictions, 'logs/newsqa_saved_data/dummy5_unsup_train_predictions_epoch_6.txt')
utils.save_lines(dev_predictions, 'logs/newsqa_saved_data/dummy5_unsup_validation_predictions_epoch_6.txt')
utils.save_lines(test_predictions, 'logs/newsqa_saved_data/dummy5_unsup_test_predictions_epoch_6.txt')




