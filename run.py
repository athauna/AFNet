import argparse
import prediction
import evaluation

def main():
    parser = argparse.ArgumentParser(description="Code for the prediction and evaluation of AFNet.")
    parser.add_argument("dataset", type=str, choices=["potsdam","vaihingen"], help="choose dataset to do prediction or evaluation.")
    parser.add_argument("mode", type=str, choices=["prediction","evaluation"], help="whether do prediction or evaluation.")
    args = parser.parse_args()
    
    if args.mode == 'prediction':
        prediction.main(args.dataset)
    if args.mode == 'evaluation':
        evaluation.main(args.dataset)

if __name__ == "__main__":
    main()
    

    


