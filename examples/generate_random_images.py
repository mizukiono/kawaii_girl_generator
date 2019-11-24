import argparse
import os
import os.path as osp

import kawaii_gen

parser = argparse.ArgumentParser()
parser.add_argument('output_dir')
parser.add_argument('--num', type=int)
args = parser.parse_args()

generator = kawaii_gen.GirlFaceGenerator()
girl_faces = generator.generate(num=args.num)

os.makedirs(args.output_dir, exist_ok=True)

for i, girl_face in enumerate(girl_faces):
    girl_face.image.save(osp.join(args.output_dir, f"{i}.png"), format="PNG")