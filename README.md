# MakeGif

gif画像を扱う時に気づいたことがあったのでメモ．

gif画像を作る時に画像を読み込む．

`img = Image.open(img_path).convert(mode)` 

その際に`.convert(mode)` するmodeによってgifのクオリティに差がでることが分かった．

今回は，以下の9つの場合について調べた．

`mode = RGBA, RGB, P, CMYK, HSV, YCbCr, F, I, L`

カラーの場合は，読み込んだ画像がRGBであってもRGBAにconvertすることで，画質を保ったままgif画像に変換可能．

白黒の場合は，F，I，Lのどの変換であっても画質を保ったままgif画像に変換可能．

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