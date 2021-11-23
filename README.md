# Kawaii Girl Generator
(For Japanese version README, go to [README_ja](https://github.com/xiong-jie-y/kawaii_girl_generator/blob/master/README_ja.md).)

The module provide a feature to generate kawaii girls.
The module currently support generating face images like below.

![Catch Image](docs/images/catch_image.jpg)

Kawaii is Japanese word and Kawaii is pronounced as [kaɰaiꜜi].
This is like cute, but have more subtle meaning.

## Usage
### Requirements
Please use this module AT YOUR OWN RISK.

* conda
* tensorflow 1.14.0 or tensorflow-gpu: 1.14.0

### Installation
One example of installation is
```bash
git clone git@github.com:xiong-jie-y/kawaii_girl_generator.git

## Create python environment
conda create -n py37_cute_girl_generator python=3.7
conda activate py37_cute_girl_generator

### if you need faster generation
conda install -y tensorflow-gpu==1.14.0
### if you are ok with slower generation
conda install -y tensorflow==1.14.0

pip install pillow

# workardoun for dnn lib
pip install requests

## Prepare model
cd kawaii_girl_generator
python scripts/prepare_models.py
pip install -e .
```

### Generate Random Girl Images
It will generate 256x256 face image.
```bash
cd kawaii_girl_generator
python examples/generate_random_images.py --num 2 output/
```

## Agreement to use
The model and the output of the model can be used in personal use.
That means only checking output in local environment is allowed.
For example, using output as a SNS icon, embedding model to app or deploying to public API is prohibited.

Licenses are under [MIT License](https://github.com/xiong-jie-y/kawaii_girl_generator/blob/master/LICENSE) except `dnnlib/`.
`dnnlib/` files are made by NVIDIA and code is from https://github.com/NVlabs/stylegan: 061cc4effdcd1da86a0cc6e61e64b575cf35ffa.
The paper is [1].

## Authors
* Xiong Jie

## Bibliography
* [1] Tero Karras (NVIDIA), Samuli Laine (NVIDIA), Timo Aila (NVIDIA), "A Style-Based Generator Architecturefor Generative Adversarial Networks", http://stylegan.xyz/paper