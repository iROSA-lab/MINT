from baselines_agents.agent_video_structure.agent import VideoStructureAgent
from tqdm import trange
import wandb

import torch
torch.autograd.set_detect_anomaly(True)

def run_experiment(model_name, params):
    print('Running experiment {0}'.format(model_name))
    config['model_name']=model_name
    wandb.init(project="MIME", name=model_name ,
                # anonymous="allow",
                config=config, 
                # mode="disabled"
                )
    agent=VideoStructureAgent(config, dataset='MIME')
    agent.train()
    for i in trange(config['evaluation_epochs'], desc='Evaluation'):
        agent.eval()
    wandb.run.finish()

config={
    'model_name':'',
    # parameters for dataset
    'tasks':'1,2,3,4',#,5,6,7,8,9,10,11,12,13,15,16,17,19,20', # 14 and 18 are not available 
    'training_demos':20,
    'evaluation_demos':5,
    'number_of_stacked_frames':2,
    'number_of_stacked_frames':16,
    'width':320, # MIME 640 -> after crop to 320x240
    'height':240, # MIME 240
    'channels':3, # RGB
    'num_frames':50, # number of frames sampled from each video
    'input_width':64,
    'input_height':64,
    # parameters for model
    'batch_size':16,
    'save_model':True,
    'load_model':False,
    'epochs':100,
    'num_keypoints':25,
    'learning_rate':0.001,
    'weight_decay':0.00005,#equivalent to L2 regularization in keras
    'padding':'same',
    'std_for_gaussian_maps':1.5,
    'evaluation_epochs':160,
    # parameters for losses
    'sigma_for_separation_loss':0.002,
    'num_encoder_filters':32,
    'heatmap_ratio':4.0,
    'layers_per_scale':2,
    'clip_value':1.0,
    # weights for losses
    'separation_loss_weight':0.02,
    'sparsity_loss_weight':0.1, # heatmap_regularization
    'reconstruction_loss_weight':0.01,
}

run_experiment(model_name='Video_structure_MIME', params={})