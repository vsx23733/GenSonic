# Image comparison script

###########################
### Comparison pipeline ###
###########################

# Extract features --> Cosine similarity 

from sklearn.metrics.pairwise import cosine_similarity
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn.functional as F
from PIL import Image


def extract_features(input_image):
    """
    Use a pretrained model to extract feature of the input image
    """
    transform = transforms.Compose([
    transforms.Lambda(lambda img: img.convert("RGB")),
    transforms.Resize((224, 224)), 
    transforms.ToTensor(), 
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    processed_input_image = transform(input_image).unsqueeze(0)
    # processed_input_image = processed_input_image.detach().numpy()

    feature_extractor = models.resnet50(pretrained=True)
    feature_extractor = torch.nn.Sequential(*list(feature_extractor.children())[:-1])
    feature_extractor = feature_extractor.eval()

    features = feature_extractor(processed_input_image)
    return features

def compute_similarity_score(img1_path, img2_path):
    """
    Compute the similarity score of the input images
    """
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    feature_img1 = extract_features(img1)
    feature_img2 = extract_features(img2)

    feature_img1 = feature_img1.detach().numpy()
    feature_img2 = feature_img2.detach().numpy()

    similarity_score = cosine_similarity(feature_img1.reshape(1, -1), feature_img2.reshape(1, -1))

    return similarity_score

def main():

    # Change path if needed
    img1_path = r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\reassembled_commercial_level.png"
    img2_path = r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\Sonic1_MD_Map_Ghz1.png"

    similarity_scores = compute_similarity_score(img1_path, img2_path)[0][0]
    print(similarity_scores)

if __name__ == "__main__":
    main()
