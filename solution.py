class solution:
    def __init__(self,predicted_class):
        self.disease = ['''BS =  Bacterial Spot:
   - Pesticide Used: Copper-based fungicides
   - Quantity: Mix 2-4 tablespoons per gallon of water
   - About the Disease: Wide occurrence in India, particularly in areas with frequent rainfall.
   - Precautions:
     - Avoid overhead irrigation to minimize water splashing.
     - Remove and destroy infected plant material promptly.''',
     '''EB = Early Blight:
   - Pesticide Used: Mancozeb
   - Quantity: Mix 2-4 tablespoons per gallon of water
   - About the Disease: Widespread in various regions of India.
   - Precautions:
     - Practice crop rotation with non-related plants.
     - Mulch around plants to prevent soil splashing.''',
     '''LB =  Late Blight:
   - Pesticide Used: Mancozeb
   - Quantity: Mix 2-4 tablespoons per gallon of water
   - About the Disease: Found in cooler and moist regions of India.
   - Precautions:
     - Apply fungicides preventively during periods of high humidity.
     - Remove and destroy infected plant material to reduce the source of spores.''',
     '''LM = Leaf Mold:
   - Pesticide Used: Copper-based fungicides
   - Quantity: Dilute according to the manufacturer's instructions
   - About the Disease: Common in areas with high humidity and moderate temperatures.
   - Precautions:
     - Provide adequate spacing for air circulation.
     - Avoid overhead irrigation.''',
     '''SLS = Septoria Leaf Spot:
   - Pesticide Used: Chlorothalonil
   - Quantity: Follow the manufacturer's instructions for dilution
   - About the Disease: Common in regions with moderate temperatures and high humidity.
   - Precautions:
     - Water the soil, not the foliage, to minimize the spread of spores.
     - Remove and destroy infected leaves promptly.''',
     
    '''SM = Spider Mites (Two-Spotted Spider Mite):
      - Pesticide Used: Insecticidal soap
      - Quantity: Follow the product instructions for dilution
      - About the Pest: Found in dry and hot regions of India.
      - Precautions:
        - Maintain proper humidity to discourage mite infestations.
        - Regularly spray plants with water to reduce mite populations.''',
     '''TS = Target Spot:
   - Pesticide Used: Chlorothalonil
   - Quantity: Follow the manufacturer's instructions for dilution
   - About the Disease: Common in warm and humid regions of India.
   - Precautions:
     - Rotate crops to reduce the risk of disease buildup.
     - Ensure proper spacing between plants for good air circulation.''',
     '''TYL = Tomato Yellow Leaf Curl Virus:
   - Pesticide Used: Imidacloprid
   - Quantity: Follow the recommended dosage on the product label
   - About the Disease: Prevalent in tropical and subtropical regions of India.
   - Precautions:
     - Use virus-resistant tomato varieties.
     - Control whitefly populations through insecticides or reflective mulches.''',
     ''' TMS=Tomato Mosaic Virus:
   - Pesticide Used: Neem oil
   - Quantity: Mix 1-2 tablespoons of neem oil with a gallon of water
   - About the Disease: Found in various locations in India, especially in areas with high humidity.
   - Precautions:
     - Use virus-free seeds and seedlings.
     - Control and manage insect vectors like aphids and whiteflies.''',
     '''TH = Tomato - Healthy:
   - No specific pesticides needed for healthy plants.
   - Preventive Measures:
     - Practice good garden hygiene.
     - Monitor plants regularly for any signs of diseases or pests.''',
   ]
        self.sol=['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight','Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
        'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tommato_mosaic_virus', 'Tomato___healthy']
    def fertilizer(self,predicted_class):
        ind= self.sol.index(predicted_class)
        return self.disease[ind]

    