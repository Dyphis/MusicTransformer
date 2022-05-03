import os
import sys
import pickle
import glob

from tqdm import tqdm
from processor import encode_midi

def preprocess_midi_files_under(midi_dir='data/', save_dir='processed/'):
    if midi_dir[-1] != '/':
        midi_dir += '/'
    if midi_dir[-1] != '/':
        midi_dir += '/'
    file_list = []
    file_list += glob.glob(midi_dir + '*.mid')
    file_list += glob.glob(midi_dir + '*.midi')
    os.makedirs(save_dir, exist_ok=True)

    for file in tqdm(file_list, desc='processing midis'):

        try:
            data = encode_midi(file)
        except KeyboardInterrupt:
            print(' Abort')
            return
        except EOFError:
            print('EOF Error')
            return
        for i in range(len(data) - 1025):

            with open('{}/{}.pickle'.format(save_dir, file.split('/')[-1]), 'wb') as f:
                pickle.dump(data, f)
            print('Piece {} generated.'.format(i))

if __name__ == '__main__':
    '''
    preprocess_midi_files_under(
            midi_dir=sys.argv[1],
            save_dir=sys.argv[2])
    '''
    print(sys.argv)