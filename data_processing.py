import glob
import csv

if __name__ == "__main__":
    
    txt_files_neg = glob.glob('../resource/lib/publicdata/aclImdb/train/neg/*.txt')
    txt_files_pos = glob.glob('../resource/lib/publicdata/aclImdb/train/pos/*.txt')

    with open('imdb_tr.csv', 'w', newline = '') as writeFile:
        writer = csv.writer(writeFile, delimiter=',')
        for ind,path in enumerate(txt_files_neg):
            try:
                raw = pd.read_csv(path, quoting = 3, error_bad_lines = False)
                raw = list(raw)
                sentence_string = ''
                for j in raw:
                    sentence_string = sentence_string + j
                output = [ind, sentence_string, 0]
                writer.writerow(output)
            except UnicodeEncodeError:
                continue

    final_ind = ind + 1 # Increasing the output index for the positive data  

    with open('imdb_tr.csv', 'a', newline = '') as writeFile:
        writer = csv.writer(writeFile, delimiter=',')
        for ind,path in enumerate(txt_files_pos):
            try:
                raw = pd.read_csv(path, quoting = 3, error_bad_lines = False)
                raw = list(raw)
                sentence_string = ''
                for j in raw:
                    sentence_string = sentence_string + j
                output = [final_ind + ind, sentence_string, 1]
                writer.writerow(output)
            except UnicodeEncodeError:
                continue