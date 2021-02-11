
import os
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\LENOVO\Documents\hackathon\Unique\ML\ku-hack-6b534f8e99ac.json"

folder_path = r"C:\Users\LENOVO\Documents\hackathon\Unique\ML"
image_path = 'test-KU.png'
path = os.path.join(folder_path, image_path)


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


detect_text(path)
