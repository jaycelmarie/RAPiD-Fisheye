## Github Repositories ##
Source code derived from: [[Duan's Repository](https://github.com/duanzhiihao/RAPiD#readme)]
My own repository: [[My Repository](https://github.com/jaycelmarie/RAPiD-Fisheye.git)]

## Installation ##
**Requirements**:
The following packages were imported in a Linux Environment:
- PyTorch >= 1.0. Installation instructions can be found at https://pytorch.org/get-started/locally/
- opencv-python
- Pycocotools -> [pycocotools](https://github.com/cocodataset/cocoapi)
- tqdm


## Testing on a single image ##
1. Clone my repository
2. Download the [pre-trained network weights](https://github.com/duanzhiihao/RAPiD/releases/download/v0.1/pL1_MWHB1024_Mar11_4000.ckpt), which is trained on COCO, MW-R and HABBOF, and place it under the RAPiD/weights folder.
If running in Virtualbox Machine in Ubuntu:
3. Refer to [OpenCV Installation](https://pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/) to install openCV on Ubuntu.
4. Run `workon -openCV setup name-` in terminal.
5. Directly run `python main.py` or `python3 main.py` in terminal.

<p align="center">
<img src="https://github.com/duanzhiihao/RAPiD/blob/master/images/readme/exhibition_rapid608_1024_0.3.jpg?raw=true" width="500" height="500">
</p>


## Citation
```
Z. Duan, M.O. Tezcan, H. Nakamura, P. Ishwar and J. Konrad, 
“RAPiD: Rotation-Aware People Detection in Overhead Fisheye Images”, 
in IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 
Omnidirectional Computer Vision in Research and Industry (OmniCV) Workshop, June 2020.
```
