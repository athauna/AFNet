# AFNet
The code of Adaptive Fusion Network for Remote Sensing Image Semantic Segmentation.

## Requirements
Platform, linux ubuntu 16.04.5 LTS <br/>
python 3.5 <br/>
tensorflow-gpu>=1.8.0 <br/>
numpy <br/>
opencv-python <br/>
tqdm <br/>
argparse<br./>

## Instructions for the folders
./data/image/potsdam/      folder for test images of the Potsdam dataset. <br/>
./data/image/vaihingen/    folder for test images of the Vaihingen dataset. <br/>
./data/label/potsdam/      folder for test labels (boundaries eroded) of the Potsdam dataset. <br/>
./data/label/vaihingen/    folder for test labels (boundaries eroded) of the Vaihingen dataset. <br/>
you can download the images and labels from the official websites of [ISPRS 2d Semantic labeling](http://www2.isprs.org/commissions/comm3/wg4/semantic-labeling.html) <br/>
After downloading the images and labels, extracting them to corresponding folders and delete the *instruction.txt* in the folder. <br/>

---------
./model/potsdam/           folder for the trained model of the Potsdam dataset. <br/>
./model/vaihingen/         folder for the trained model of the Vaihingen dataset. <br/>
After downloading the models, extracting them to corresponding folders and delete the *instruction.txt* in the folder. <br/>

---------
./result/potsdam/          folder for the predictions of the Potsdam dataset.<br/>
./result/vaihingen/        folder for the predictions of the Vaihingen dataset. <br/>
./result/                  folder for the accuracy statistics for the two datasets. The statistics will be generated after running the evaluation code. <br>
The predictions of both datasets could be obtained either by running prediction code or download form hyperlink.

---------
**Notice** Remove all *instruction.txt* in folders before running.
---------

## Running code
Generally, the prediction should be done before evaluation, unless the predictions have been downloaded. Before running prediction, the aforementioned test images should be placed in the correct folder, and the *instruction.txt* should be deleted.
If you want to run predictions yourself, you can run the following script: <br/>
'python run.py dataset prediction'
where *dataset* has two optional values, *potsdam* and *vaihingen*, on which dataset the prediction will be conducted. The predictions will be output in the ./result/*dataset*/ folder. <br/>
If there are predictions on the corresponding folders, after the labels (boundaries eroded) have been placed correctly, and the *instruction.txt* has been removed from the label folder, we can test the accuracy of predictions by the following script:<br/>
'python run.py dataset evaluation'
where *dataset* has two optional values, *potsdam* and *vaihingen*, on which dataset the evaluation will be conducted. The statistics are recorded in the *.txt* file under the ./result/ folder.
**Notice** The evaluation code is implemented in Python, but it is consistent with the results of the official test code released by ISPRS. You can also run the official test code to do an evaluation. Apart from OA and F1 calculated in the official test code, the IoU is calculated in our evaluation code. The code for IoU calculation refers to [ADE20k](https://github.com/CSAILVision/sceneparsing/tree/master/evaluationCode), and we have made some minor changes.
