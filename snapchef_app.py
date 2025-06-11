import streamlit as st

# Set up page
st.set_page_config(page_title="SnapChef 🍽️", page_icon="🍽️")
st.title("🍽️ SnapChef")
st.subheader("Choose a South Indian dish and get the full recipe!")

# Local recipe database
recipes = {
    'idli': {
        'image': 'https://www.tomatoblues.com/wp-content/uploads/2018/07/SAMAI-IDLI-1-scaled.jpg',
        'ingredients': ['2 cups rice', '1 cup urad dal', 'Salt', 'Water'],
        'steps': [
            'Soak rice and urad dal separately for 6 hours.',
            'Grind to a smooth paste and mix.',
            'Ferment overnight.',
            'Pour batter into idli plates and steam for 10-12 minutes.'
        ]
    },
    'dosa': {
        'image': 'https://media.cntraveller.in/wp-content/uploads/2020/05/dosa-recipes-1366x768.jpg',
        'ingredients': ['3 cups rice', '1 cup urad dal', 'Fenugreek seeds', 'Salt'],
        'steps': [
            'Soak rice, urad dal, and fenugreek for 6 hours.',
            'Grind into smooth batter.',
            'Ferment overnight.',
            'Spread on hot pan and cook till golden.'
        ]
    },
    'uttapam': {
        'image': 'https://i.pinimg.com/originals/9e/08/46/9e0846d1734e66d2e383e1096c5b64ef.jpg',
        'ingredients': ['Dosa batter', 'Onion', 'Tomato', 'Chili', 'Coriander'],
        'steps': [
            'Pour batter on pan like thick pancake.',
            'Top with chopped vegetables.',
            'Cook both sides till crisp.'
        ]
    },'medu vada': {
        'image': 'https://myfoodstory.com/wp-content/uploads/2022/09/Medu-Vada-2-1024x1536.jpg',
        'ingredients': ['1 cup urad dal', 'Onion', 'Curry leaves', 'Black pepper', 'Salt'],
        'steps': [
            'Soak and grind urad dal.',
            'Add spices and shape like donuts.',
            'Deep fry until golden brown.'
        ]
    },
    'pongal': {
        'image': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/01/pongal-ven-pongal.jpg',
        'ingredients': ['1 cup rice', '1/4 cup moong dal', 'Ghee', 'Pepper', 'Cumin', 'Ginger'],
        'steps': [
            'Cook rice and dal together.',
            'Fry spices in ghee and mix.',
            'Serve hot with chutney.'
        ]
    },
    'upma': {
        'image': 'https://simpleindianmeals.com/wp-content/uploads/2014/02/Rava-Upma.jpg',
        'ingredients': ['1 cup rava', 'Onion', 'Green chili', 'Mustard seeds', 'Curry leaves'],
        'steps': [
            'Roast rava lightly.',
            'Temper spices and onions.',
            'Add water and rava.',
            'Stir and cook until thick.'
        ]
    },
    'bisibelebath': {
        'image': 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/07/bisi-bele-bath-recipe.jpg',
        'ingredients': ['Rice', 'Toor dal', 'Tamarind', 'Vegetables', 'Spices'],
        'steps': [
            'Cook rice and dal separately.',
            'Boil vegetables with tamarind.',
            'Add spice mix and combine all.',
            'Simmer and serve hot.'
        ]
    },
    'sambar': {
        'image': 'https://www.cubesnjuliennes.com/wp-content/uploads/2021/01/South-Indian-Sambar-Recipe.jpg',
        'ingredients': ['Toor dal', 'Tamarind', 'Sambar powder', 'Vegetables', 'Mustard seeds'],
        'steps': [
            'Cook dal and mash.',
            'Boil vegetables with tamarind.',
            'Add dal, spices and simmer.',
            'Temper with mustard and curry leaves.'
        ]
    },
    'rasam': {
        'image': 'https://www.blueberriesfoods.com/wp-content/uploads/2018/10/rasam-1.png',
        'ingredients': ['Tamarind juice', 'Tomato', 'Rasam powder', 'Coriander', 'Mustard seeds'],
        'steps': [
            'Boil tamarind with tomato and spices.',
            'Add tempering of mustard and curry leaves.',
            'Serve hot with rice.'
        ]
    },
    'lemon rice': {
        'image': 'https://vegecravings.com/wp-content/uploads/2018/02/Lemon-Rice-Recipe-Step-by-Step-Instructions.jpg',
        'ingredients': ['Cooked rice', 'Mustard seeds', 'Green chili', 'Lemon juice', 'Curry leaves'],
        'steps': [
            'Temper mustard, chili, and curry leaves.',
            'Add rice and salt.',
            'Mix with lemon juice and serve.'
        ]
    },
    'curd rice': {
        'image': 'https://d36v5spmfzyapc.cloudfront.net/wp-content/uploads/2021/01/south-indian-curd-rice-2.jpg',
        'ingredients': ['Cooked rice', 'Curd', 'Mustard seeds', 'Ginger', 'Curry leaves'],
        'steps': [
            'Mix rice and curd.',
            'Add tempering of mustard and ginger.',
            'Chill and serve.'
        ]
    },
    'tamatar rice': {
        'image': 'https://c.ndtvimg.com/2021-08/mtuo47so_tomato-rice_625x300_16_August_21.jpg',
        'ingredients': ['Rice', 'Tomatoes', 'Onion', 'Garlic', 'Spices'],
        'steps': [
            'Cook onions and tomatoes with spices.',
            'Mix with cooked rice.',
            'Garnish with coriander.'
        ]
    },
    'avial': {
        'image': 'https://recipes.timesofindia.com/photo/61604457.cms',
        'ingredients': ['Mixed vegetables', 'Coconut', 'Curd', 'Curry leaves'],
        'steps': [
            'Boil vegetables.',
            'Add ground coconut and curd.',
            'Simmer gently and add curry leaves.'
        ]
    },
    'adai': {
        'image': 'https://farm4.staticflickr.com/3766/9407059376_9970d43532_b.jpg',
        'ingredients': ['Rice', 'Chana dal', 'Toor dal', 'Red chili', 'Curry leaves'],
        'steps': [
            'Soak and grind ingredients.',
            'Make thick dosa on tawa.',
            'Serve with chutney.'
        ]
    },
    'kootu': {
        'image': 'https://3.bp.blogspot.com/-68Qz0RPvC1I/UmUDsB4e-MI/AAAAAAAABzU/duKRLXDdXDY/s1600/Podalangai+Kootu.jpg',
        'ingredients': ['Vegetables', 'Moong dal', 'Coconut', 'Cumin', 'Green chili'],
        'steps': [
            'Cook dal and vegetables.',
            'Add coconut-cumin paste.',
            'Boil and temper with mustard.'
        ]
    },
    'kozhukattai': {
        'image': 'https://thefamiliarkitchen.com/wp-content/uploads/2020/04/IMG_2861-scaled.jpg',
        'ingredients': ['Rice flour', 'Jaggery', 'Coconut', 'Cardamom'],
        'steps': [
            'Make stuffing with jaggery and coconut.',
            'Make dough with rice flour.',
            'Fill and steam for 10-12 minutes.'
        ]
    },
    'puliyogare': {
        'image': 'https://vanitascorner.com/wp-content/uploads/2023/05/puliyogare-500x375.jpg',
        'ingredients': ['Tamarind', 'Spices', 'Curry leaves', 'Peanuts', 'Cooked rice'],
        'steps': [
            'Make tamarind paste with spices.',
            'Mix with rice and peanuts.',
            'Serve warm.'
        ]
    },
    'appam': {
        'image': 'https://thefamiliarkitchen.com/wp-content/uploads/2019/02/img_3166-2048x2048.jpg',
        'ingredients': ['Rice', 'Coconut', 'Yeast', 'Sugar', 'Salt'],
        'steps': [
            'Soak and grind rice with coconut.',
            'Ferment overnight with yeast.',
            'Pour in appam pan and cook.'
        ]
    },
    'puttu': {
        'image': 'https://www.vegrecipesofindia.com/wp-content/uploads/2017/11/puttu-recipe-500x500.jpg',
        'ingredients': ['Rice flour', 'Grated coconut', 'Water', 'Salt'],
        'steps': [
            'Mix rice flour with water.',
            'Layer with coconut in puttu steamer.',
            'Steam for 5-7 minutes.'
        ]
    },
    
    'mysore pak': {
        'image': 'https://cdn.cdnparenting.com/articles/2019/02/19092259/Mysore-Pak-Recipe-3467583981.jpg',
        'ingredients': ['Besan', 'Ghee', 'Sugar', 'Water'],
        'steps': [
            'Make sugar syrup.',
            'Add besan and ghee slowly.',
            'Cook until it thickens.',
            'Pour in tray and cut into pieces.'
        ]
    },
    
}


dish_list = list(recipes.keys())
dish_list.sort()


selected_dish = st.selectbox("Select a dish:", options=dish_list)


if selected_dish:
    data = recipes[selected_dish]
    
    st.image(data['image'], width=300, caption=selected_dish.capitalize())
    
    st.markdown("### 📋 Ingredients")
    for ing in data['ingredients']:
        st.write(f"• {ing}")

    st.markdown("### 🧑‍🍳 Preparation Steps")
    for i, step in enumerate(data['steps'], 1):
        st.write(f"{i}. {step}") 
