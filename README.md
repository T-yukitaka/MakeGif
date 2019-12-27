# MakeGif

gif画像を扱う時に気づいたことがあったのでメモ．

gif画像を作る時に
`Image.open(img_path).convert(mode)`

## Results
| RGBA | RGB | P |
----|----|----
| <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/RGBA.gif'> | <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/RGB.gif'> | <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/P.gif'> |

| CMYK | HSV | YCbCr |
----|----|----
| <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/CMYK.gif'> | <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/HSV.gif'> | <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/YCbCr.gif'> |

| F | I | L |
----|----|----
| <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/F.gif'> | <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/I.gif'> | <img src='https://github.com/T-yukitaka/MakeGif/blob/master/results/L.gif'> |


## Prerequisites
- Linux or macOS
- python 3

## Getting Started
### Instalattion
- Clone this repo:
```
git clone https://github.com/T-yukitaka/MakeGif.git
cd MakeGif
```
- Generate images:
```
python GenerateImgs.py
```
- Make gif images:
```
python MakeGif.py
```