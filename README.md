## Usage
### Installation
### Example
#### Generate and save two random girl face images
```python
import kawaii_gen

generator = kawaii_gen.GirlFaceGenerator()

girl_faces = generator.generate(num=2)

for girl_face in girl_faces:
    girl_face.image.save()
```