import time
import pickle

import numpy as np
import PIL

import dnnlib
import dnnlib.tflib as tflib

tflib.init_tf()

class GirlFace:
    def __init__(self, image, latent_vector):
        self.image = image
        self.latent_vector = latent_vector

class GirlFaceGenerator:
    def generate(self, num, seed=int(time.time()), use_gpu=False):
        """Generate random girl faces.

        Args:
            num: The number of faces generated.
            seed: The seed to be used in the func.

        Returns:
            The generator of GirlFace randomly generated.
        """
        _G, _D, Gs = pickle.load(open('models/sgan-256.pkl', 'rb'))
 
        latents = np.random.RandomState(seed).randn(num, Gs.input_shape[1])

        synthesis_kwargs = dict(
            output_transform=dict(
                func=tflib.convert_images_to_uint8, 
                nchw_to_nhwc=False
            ), 
            minibatch_size=8,
            use_gpu=use_gpu,
        )

        images = Gs.run(latents, None, **synthesis_kwargs)

        for image, latent_vec in zip(images, latents):
            image = PIL.Image.fromarray(image, 'RGB')
            yield GirlFace(image, latent_vec)
