import argparse
import os
import shutil

def main(args):
    output_path = "model_logs"
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for file in os.listdir(args.path):
        if os.path.isdir(os.path.join(args.path, file)):
            if not os.path.exists(os.path.join(output_path, file)):
                os.mkdir(os.path.join(output_path, file))
            for f in os.listdir(os.path.join(args.path, file)):
                if file == "0_BERT":
                    shutil.copy(os.path.join(args.path, file, f), os.path.join(output_path, file, "bert_"+f))
                elif file == "1_Pooling":
                    shutil.copy(os.path.join(args.path, file, f), os.path.join(output_path, file, "pooling_"+f))
                else:
                    raise ValueError("Unexpected folder - '{}'".format(file))
        else:
            shutil.copy(os.path.join(args.path, file), os.path.join(output_path, file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True, help="Files to transform. This files are inside model_results folder of the project")
    args = parser.parse_args()
    main(args)
    