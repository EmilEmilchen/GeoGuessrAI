from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("geolocal/StreetCLIP")
processor = CLIPProcessor.from_pretrained("geolocal/StreetCLIP")

choices = ["Åland", "Albania", "American Samoa", "Andorra", "Argentina", "Australia", "Austria", "Bangladesh",
           "Belgium", "Bermudas", "Bhutan", "Bolivia", "Botswana", "Brazil", "Bulgaria", "Cambodia", "Chile",
           "Christmas Islands", "Colombia", "Costa Rica", "Croatia", "Curacao", "Czech Republic", "Denmark",
           "Dominican Republic", "Ecuador", "Estonia", "Eswatini", "Faroe Islands", "Finland", "France", "Germany",
           "Ghana", "Gibraltar", "Greece", "Greenland", "Guam", "Guatemala", "Hong Kong", "Hungary", "Iceland", "India",
           "Indonesia", "Ireland", "Isle of Man", "Israel", "Italy", "Japan", "Jersey", "Jordan", "Kenya", "Kyrgyzstan",
           "Laos", "Latvia", "Lesotho", "Lithuania", "Luxembourg", "Macau", "Malaysia", "Malta", "Mexico", "Monaco",
           "Mongolia", "Montenegro", "Netherlands", "New Zealand", "Nigeria", "North Macedonia",
           "Northern Mariana Islands", "Norway", "Palestine", "Peru", "Philippines", "Pitcairn Islands", "Poland",
           "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "San Marino", "Senegal",
           "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa", "South Korea", "Spain", "Sri Lanka", "Sweden",
           "Switzerland", "Taiwan", "Thailand", "Tunisia", "Türkiye", "Uganda", "Ukraine", "United Arab Emirates",
           "United Kingdom", "United States Virgin Islands", "Uruguay", "USA", "United States of America", "Curaçao",
           "Turkiye", "Aland"]


def identify(image, count):
    inputs = processor(text=choices, images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # this is the image-text similarity score

    outputs = logits_per_image[0]

    # Get the indices that would sort the tensor in descending order
    sorted_indices = torch.argsort(outputs, descending=True)

    # 'second_highest_index' will contain the index of the second-highest value in the tensor.
    result = [[], []]
    for i in range(0, count):
        result[0].append(choices[sorted_indices[i].item()])
        result[1].append(outputs[sorted_indices[i].item()].detach().numpy().tolist())

    return result


def print_results(results):
    for (country, probability) in zip(results[0], results[1]):
        print(country, probability)
