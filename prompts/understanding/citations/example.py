import boto3
import json

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )

response = bedrock_runtime.converse(
                modelId='us.amazon.nova-lite-v1:0',
                system=[{"text": """You are an AI assistant that answers questions about documents and 
correctly cites your sources of information in the document. 
Follow these instructions:
1. Read and understand the question asked under <question>.
2. Read through the <document_content> and find the answer to the question. 
3. Think step-by-step about how the <document_content> may or may not answer the question, and put your thoughts in <thinking> tags
4. If you find an answer in the document, format your citation in a list as follows and put into <citation> tags: 
    [
        {
            "pageNumber": "the number of the pages where the answer was found",
            "text": "The literal, verbatim text found that answers the question",
            "section": "A best effort description of the section where the answer was found"
        }
    ]
5. Put your answer in <answer> tags, and ground it in facts using only whats in <document_content>
6. If you can't find the answer in the text, just say empty answer tags <answer></answer>. Its ok if you can't find the answer!
"""}],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": f"""
<document_content>
1
EAT REAL
RECIPES FROM SOME OF  
AMERICA’S BEST CHEFS
Center  for SCienCe in the Publi C intere St
I
Food Day Recipes
Table of ContentsFood Day is a celebration, and what would a celebration, especially one about food, be without 
delicious food.  We’ve adapted a variety of delicious, healthy, easy-to-prepare recipes from some of 
the country’s most prominent chefs and cookbook writers.  Choose seasonal, locally grown, and 
organic ingredients when possible.  If you are celebrating Food Day, October 24, with a dinner 
or potluck at your home, please consider using some of these recipes—but, of course, you can 
cook them any other day, too.  They’ll brighten up your dinner table and delight your taste buds.
SOUPS
Fennel & Apple Soup  .................................................................................................... 1
Carrot, Sweet Potato & Ginger Soup  ................................................................... 25
SALADS 
Squash & Mushroom Salad  ........................................................................................ 4
Green Bean Salad with Red Onion & Salsa Dressing  ...................................... 5
Sweet & Tangy Three Bean Salad  ......................................................................... 10
Lentil, Apple & Walnut Salad with Cider Dressing  .......................................... 19
Shredded Tuscan Kale Tomato & Avocado Salad  ........................................... 26
SIDES
Green Beans with Charred Onions  ......................................................................... 2
Mussels with Pepperonata  ......................................................................................... 3
Sweet Potato & Caramelized Onions with Chili Dressing  .............................. 6
Couscous with Dried Cranberries & Pecans  ....................................................... 8
Tuscan Kale & White Bean Ragout  ........................................................................ 14
Braised Kohlrabi with Fennel & Leeks  .................................................................. 16
Rosemary-Orange Cauliflower Puree  ................................................................... 17
Pomegranate-Cinnamon Tabbouleh  ..................................................................... 18
Pearl Barley with Spinach Pesto  .......................................................................... 20
Spicy Garlic Broccoli with Pine Nuts  ................................................................... 23
MAINS
Quick Tostados  .............................................................................................................. 7
Autumn Vegetable Curry  ........................................................................................... 11
Honey-Crisp Oven-Fried Chicken  .......................................................................... 12
Gumbo with Smoked Turkey & Wild Rice  ........................................................... 15
Hot & Sour Salmon with Greens  ............................................................................ 22
Rainbow Salad with Spicy Peanut Dressing  ..................................................... 24
Curried Lentils with Walnuts, Spinach & Cherry Tomatoes  ........................ 27
Oven Roasted Stuffed Portobello Mushrooms  ................................................ 28
DESSERTS
Baked Pumpkin Orange Custard  ............................................................................. 9
Apple Crisp  ..................................................................................................................... 13
Yogurt Panna Cotta with Cranberry Pear Sauce  ............................................. 21
IIDAN BARBER
Dan Barber is the chef and owner of the Blue Hill and Blue 
Hill at Stone Barns restaurants. He is also an accomplished 
writer on the topic of food and agriculture policy and was 
recently appointed to serve on President Barack Obama’s 
Council on Physical Fitness, Sports and Nutrition.
MARIO BATALI
Mario Batali is a Food Network chef and star of Molto Gusto , 
Iron Chef , and a number of other shows. He owns several 
restaurants around the world and has penned cookbooks such 
as Simple Italian Foods  and Spain…A Culinary Roadtrip  with 
Gwyneth Paltrow.
RICK BAYLESS
Chef Bayless is known for his expertise on Mexican cuisine. 
He has written several cookbooks including Mexican Everyday  
and Mexican Kitchen: Capturing the Vibrant Flavors of a World-
Class Cuisine . Most recently, he appeared on the popular Bravo 
TV show Top Chef Masters. 
MARK BITTMAN
Mark Bittman is a well-known food journalist and regular 
contributor to The New York Times . He authored How to Cook 
Everything , and is a self-proclaimed “home cook” who has 
cooked with some of the world’s top chefs.
ELLIE KRIEGER
This Food Network star is a registered dietician known for 
her health-conscious and delicious dishes. She stars in Healthy 
Appetite with Ellie Krieger , and is also author of the best-selling 
cookbook So Easy: Luscious Healthy Recipes for Every Meal of the 
Week  and Comfort Food Fix: Feel Good Favorites Made Healthy. EMERIL LAGASSE
Emeril is known for his big personality and flavorful food. He 
has appeared on nearly 3,000 shows on The Food Network 
and has made a number of other television appearances.  He is 
chef-proprietor of 12 restaurants across the country as well as 
his main restaurant, Emeril’s, in New Orleans.
LYNNE ROSSETTO KASPER
Lynne Rosetto Kasper is an acclaimed food writer and host 
of the radio show The Splendid T able .  She has penned several 
books about healthy eating including bestseller The Splendid 
T able , which won both the James Beard and Julia Child 
Cookbook of the Year awards in 1994.
KATE SHERWOOD
Kate is the culinary director of Nutrition Action Healthletter, 
the world’s largest-circulation health and nutrition newsletter. 
T rained at the Culinary Institute of America, Kate has been a 
freelance food stylist at The Food Network.
MARIE SIMMONS
Marie Simmons is an award-winning cookbook author, 
cooking teacher, and food writer from the Bay Area.  She was 
a columnist for Bon Appetit magazine for 18 years and has 
written many popular cookbooks, the most recent of which is 
Things Cooks Love .
NINA SIMONDS
Nina Simonds is well-known for her Spices of Life  blog and 
scintillating cookbooks such as A Spoonful of Ginger . She 
specializes in healthy eating and is known in the culinary 
world as an expert on Asian cuisine.Food Day’s Recipe 
Contributors
Center for Science in the Public Interest   |   1220 L Street, NW, Suite 300, Washington, DC 20005
This booklet was compiled by the Center for Science in the Public Interest, sponsor of national Food Day. Where indicated, recipes were adapted by Kate Sherwood.  
For further information visit www.cspinet.org or www.FoodDay.org.
© 2011 by Center for Science in the Public Interest.
III“One of the best things you can do for your health is to cook and 
enjoy family meals made with fresh, colorful seasonal ingredients,” 
said chef and author Ellie Krieger, host of Healthy Appetite on the 
Food Network and a member of the Food Day advisory board.  “Food 
Day is a chance to celebrate the power good food has to nourish us 
and bring us together.”  
“Food Day is a great opportunity for restaurants to show their 
commitment to locally produced artisan foods, to showcase a variety 
of whole grains, and to reach out to an audience hungry for more 
sustainable ways to consume that are more in keeping with the health 
of our bodies and our environment,” said Ellen Gray, co-owner, along 
with her husband Todd Gray, of Equinox Restaurant, Watershed, and 
Todd Gray’s Muse at the Corcoran, all in Washington, D.C.
“Why Food Day? It is time to make real food the number-one priority 
in our country,” said Alice Waters, proprietor of the acclaimed Chez 
Panisse restaurant in Berkeley, Calif.  “The choices we make about 
food affect our health, the health of the planet—and the way we live 
our lives.”
WHAT CHEFS  
ARE SAYING  
ABOUT  
FOOD DAY
1DAN BARBER’S FALL RECIPE
Fennel & Apple Soup
Adapted for Food Day
Makes about 8 cups
INGREDIENTS
1 onion, minced
3 small shallots, minced
3 fennel bulbs, diced
1 apple, peeled, cored and diced
3 tablespoons extra-virgin olive oil
1 tablespoon fennel seed
1 quart vegetable stock or low-sodium broth
½ teaspoon fresh thyme leaves
½ teaspoon salt 
Freshly ground black pepper
DIRECTIONS
1. Gently sauté the onion and shallots in 1 tablespoon olive oil without browning them. 
2. Add the fennel and apple. Season with pepper. 
3. Stir in the fennel seeds and cover with stock. Simmer for 30 minutes. 
4. Add thyme, and season with up to ½ teaspoon salt and more pepper to taste. 
5. T ransfer to a blender and puree, adding remaining 2 tablespoons olive oil.
Per Serving (1 cup): Calories 110; Total Fat 6 g; Sat Fat 0.5 g; Protein 2 g; Carbs 14 g; Fiber 4 g;  Cholesterol 0 mg;  Sodium 260 mg.
2MARIO BATALI’S ITALIAN RECIPES
Green Beans with Charred Onions 
Adapted from Molto Gusto  by Mario Batali
Makes 6 servings
INGREDIENTS
1 pound green beans or haricots verts 
2 medium sweet onions, such as Vidalia or Walla Walla 
1½ tablespoons balsamic vinegar 
1½ tablespoons orange juice 
2 tablespoons extra-virgin olive oil 
¼ teaspoon Maldon or flaky sea salt 
DIRECTIONS
1. Bring 4 quarts of water to a boil in a large pot. Add the beans and blanch until  
crisp-tender, 3 to 5 minutes. Drain in a colander and cool under cold running water;  
drain well. 
2. Halve the onions lengthwise and trim off the ends. Cut lengthwise into ½-inch-wide slices. 
Heat a dry 12-inch sauté pan over medium-high heat until very hot. Add the onions and 
sauté until charred in spots but still crunchy, 4 to 6 minutes. During the last minute or so, 
add the beans, stirring and tossing to warm them through. 
3. T ransfer the beans and onions to a large bowl. Whisk the balsamic vinegar, orange juice, 
and oil together in a small bowl. Pour over the beans and onions, tossing to coat. Let stand 
for at least 10 minutes, or up to 1 hour, before serving. Sprinkle the beans with salt and 
serve.
Per Serving: Calories 80; Fat 4.5 g; Sat Fat 0.5 g; Protein 2 g; Carbs 10 g; Fiber 3 g; Cholesterol 0 mg; Sodium 90 mg. 
 
3Mussels with Peperonata 
Adapted from Molto Gusto  by Mario Batali
Makes 8 servings
INGREDIENTS
5 garlic cloves, thinly sliced 
½ cup extra-virgin olive oil 
1 pound red bell peppers (3 large), cored, seeded, and cut into ½-inch dice 
1 pound green bell peppers (3 large), cored, seeded, and cut into ½-inch dice 
1 red finger chile or serrano chile, thinly sliced 
¾ cup dry white wine 
2 pounds PEI* or other small mussels, scrubbed and debearded 
1 cup no-salt-added diced tomatoes, simmered until reduced by half 
¼ teaspoon Maldon or other flaky sea salt 
DIRECTIONS
1. Combine half the garlic and ¼ cup of the oil in a 12-inch sauté pan and heat over medium-
low heat just until the garlic is slightly softened, about 1 minute; do not allow to color. 
2. Add the bell peppers and sliced chili and cook, stirring occasionally, until the peppers are 
softened, 15 to 20 minutes. 
3. T ransfer to a medium bowl and let cool. Combine the remaining ¼ cup oil and the 
remaining garlic in a large pot and cook, stirring, over medium-high heat just until the 
garlic is slightly softened, about 1 minute. Add the wine and mussels, cover, and steam 
until the mussels open, about 4 minutes; transfer the mussels to a bowl as they open. 
4. Remove the pot from the heat and set aside. Add the tomato sauce and pepper mixture 
to the mussel broth and bring to a simmer. Season with the salt, remove from the heat, 
and gently stir in the mussels. Serve warm or at room temperature. (The mussels can be 
refrigerated for up to 3 days; serve cold, or bring to room temperature before serving.)
Per Serving : Calories 270; Fat 16 g; Sat Fat 2.5 g; Protein 15 g; Carbs 13 g; Fiber 2 g; Cholesterol 30 mg; Sodium 390 mg. 
*Prince Edward Island 
4Squash & Mushroom Salad  
Adapted from Molto Gusto  by Mario Batali
Makes 6 servings
INGREDIENTS
1 small butternut squash (about 1¼ pounds), peeled, seeded, and cut into ½-inch pieces 
½ pound baby shiitake mushroom caps, left whole, or larger caps, cut into ¼-inch-thick slices
3 large shallots, cut into ¼-inch dice 
¼ cup extra-virgin olive oil 
½ teaspoon Maldon or other flaky sea salt 
Coarsely ground black pepper 
1 tablespoon truffle oil or extra-virgin olive oil 
2 tablespoons balsamic vinegar 
Juice of 1 lemon 
1 teaspoon minced fresh rosemary 
¼ pound cremini mushrooms, trimmed and thinly sliced 
DIRECTIONS
1. Preheat the broiler. Combine the squash, shiitake mushrooms, and shallots in a large bowl. 
Add the oil, tossing to coat. Season with salt and pepper. 
2. Spread the vegetables out on a large baking sheet and broil, stirring occasionally, until the 
squash is slightly charred and just tender, 15 to 20 minutes. T ransfer to a serving bowl. 
3. Meanwhile, whisk the balsamic vinegar, lemon juice, truffle (or extra-virgin) oil, and 
rosemary together in a small bowl. 
4. Scatter the cremini over the warm salad and add the vinaigrette, tossing to coat. Serve warm 
or at room temperature.
Per Serving: Calories 140; Fat 9 g; Sat Fat 1.5 g; Protein 2 g; Carbs 14 g; Fiber 3 g; Cholesterol 0 mg; Sodium 170 mg.
 
5MEXICAN RECIPES FROM RICK BAYLESS  
Green Bean Salad with Red Onion & Salsa Dressing
Adapted from Mexican Everyday by Rick Bayless
Makes 6 servings
INGREDIENTS
1 pound green beans, trimmed
1 small red onion, thinly sliced
3 tablespoons olive oil
3 tablespoons bottled salsa, preferably green tomatillo salsa
2 teaspoons fresh lime juice
3 sprigs cilantro, plus more for garnish
¼ teaspoon kosher salt
DIRECTIONS
1. Steam the green beans until tender-crunchy, about 3 minutes. Allow them to cool then toss 
with the red onion in a large bowl.  
2. Combine the remaining ingredients in a blender or mini food processor. Process until 
smooth. 
3. Toss the dressing with the green beans and red onion.
4. Garnish with some cilantro leaves. 
Per Serving: Calories 90; Fat 7 g; Sat Fat 1 g; Protein 1 g; Carbs 7 g; Fiber 2 g; Cholesterol 0 mg; Sodium 140 mg. 
6Sweet Potato with Caramelized Onions &  
Guajillo Chili Dressing
Adapted from Mexican Everyday by Rick Bayless
Makes 6 servings
INGREDIENTS
1/3 cup olive oil
1 dried guajillo* chili, stem and seeds removed
1 clove garlic
2 tablespoons balsamic vinegar
½ teaspoon kosher salt
1 large red onion, chopped
2 pounds sweet potato, cut into ½-inch cubes
DIRECTIONS
1. Pour the oil into a very large skillet and set over medium heat. When the oil is warm, add 
the chili and garlic. T urn and stir until the chili is toasty smelling (about 30 seconds). 
Remove from the heat.  
2. Put the chili in a blender with the vinegar and salt.  Blend for 30 seconds. When the oil and 
garlic are cool, add to the blender.  Set the skillet aside without washing. Blend the dressing 
until smooth.
3. Return the skillet (it will have a light coating of oil) to medium heat and add the onion. 
Cook, stirring regularly, until soft and richly brown, 9-10 minutes. 
4. Add the sweet potatoes. Blend the dressing for a few more seconds and add to the skillet 
with the potatoes. Stir well. Cover and cook until the potatoes are tender, about 10 
minutes. Uncover and allow to cool.  Taste and adjust the seasoning. 
Per Serving: Calories 240; Fat 12 g; Sat Fat 1.5 g; Protein 3 g; Carbs 31 g; Fiber 5 g; Cholesterol 0 mg; Sodium 240 mg.
* You can use any mild or medium dried chili. 
7Quick Tostados*
Adapted from Mexican Everyday by Rick Bayless
Makes 6 servings
INGREDIENTS
1 tablespoon canola oil
2 cloves garlic, minced
2 15-ounce cans no-salt-added black beans
¼ teaspoon kosher salt
2 cups cooked shredded chicken breast or diced smoked tofu
6 cups shredded romaine
¼ cup low-fat sour cream
2 tablespoons Mexican hot sauce
12 tostados
1 avocado, diced
½ cup grated Mexican cheese (queso anejo or blanco)
½ cup chopped cilantro 
DIRECTIONS
1. Heat the oil in a medium skillet over medium heat. Add the garlic and stir for about a 
minute. Then add the beans with their liquid.  Mash the beans with a potato masher or the 
back of a spoon until you have a coarse puree, then cook, stirring regularly, until the beans 
are thickened just enough to hold their shape in a spoon, about 10 minutes.  Taste and add 
up to ¼ teaspoon salt.
2. Place the romaine in a large bowl. Mix together the sour cream and hot sauce. Drizzle over 
the romaine and toss to combine. 
3. Spread each tostado with a portion of beans.  Top with chicken and lettuce. Dot with 
avocado. Sprinkle with cheese and cilantro.  Serve right away with more hot sauce for 
doctoring.
Per Serving: Calories 420; Fat 18 g; Sat Fat 4 g; Protein 24 g; Carbs 42 g; Fiber 12 g; Cholesterol 40 mg; Sodium 430 mg. 
*Tostados are flat, crisp-fried corn tortillas.
 
8MARK BITTMAN’S AUTUMN RECIPES  
Couscous Salad with Dried Cranberries & Pecans 
From Food Matters Cookbook by Mark Bittman
Makes 4 servings 
INGREDIENTS
1 cup couscous, preferably whole wheat
Salt
2 large carrots, grated 
½ cup chopped pecans 
½ cup dried cranberries 
¼ cup chopped scallions 
¼ cup olive oil, or more as needed 
Grated zest and juice of 1 lemon, or more juice as needed 
1 teaspoon coriander 
Pinch of cayenne, or to taste 
Black pepper 
½ cup chopped fresh parsley 
1 tablespoon chopped fresh sage, or 1 teaspoon dried
DIRECTIONS
1. Put the couscous in a small pot and add 1½ cups water and a pinch of salt. Bring the water 
to a boil, then cover and remove from the heat. Let steep for at least 10 minutes, or up to 
20. 
2. Put the slightly cooled couscous in a large salad bowl along with the carrots, pecans, 
cranberries, scallions, oil, and lemon zest and juice and sprinkle with the spices and pepper. 
Use 2 big forks to combine, fluffing the couscous and tossing gently to separate the grains. 
(The salad can be made up to this point and refrigerated for up to a day; bring to room 
temperature before proceeding.) 
3. Stir in the parsley and sage. Taste and adjust the seasoning, moisten with a little more oil 
and lemon juice as you like, and serve. 
Per Serving (with ¾ teaspoon salt): Calories 450; Fat 24  g; Sat Fat 3 g; Protein 9 g; Carbs 56 g; Fiber 10 g; Cholesterol 0 mg; Sodium 390 mg. 
9Baked Pumpkin-Orange Custard 
From Food Matters Cookbook by Mark Bittman
Makes 6-8 servings 
INGREDIENTS
2 tablespoons unsalted butter, melted, plus more for greasing the pan 
2 eggs 
¾ cup brown sugar 
12 ounces soft silken tofu
3 cups (two 15-ounce cans) puréed pumpkin (unsweetened and unseasoned) 
½ teaspoon cinnamon, or more to taste 
¼ teaspoon nutmeg 
¼ teaspoon allspice 
Grated zest and juice of 1 orange 
Pinch of salt 
DIRECTIONS
1. Heat the oven to 350°F . Grease an 8- or 9-inch square pan or pie plate with a little butter. 
Use an electric mixer or a whisk to beat the eggs and sugar in a large bowl until light. Add 
the tofu and beat until smooth, a minute or 2 longer. 
2. Add the 2 tablespoons melted butter and remaining ingredients and beat until everything 
is thoroughly combined. Pour the mixture into the prepared pan and bake until set around 
the edges but still a little jiggly at the center, about 1 hour. Let cool completely before 
serving, or refrigerate for up to a day and serve cold.
Per Serving (for 1/8  of the custard): Calories 180; Fat 5 g; Sat Fat 2.5 g; Protein 5 g; Carbs 30 g; Fiber 3 g; Cholesterol 55 mg; Sodium 30 mg. 
10ELLIE KRIEGER’S COMFORT FOOD
Sweet & Tangy Three Bean Salad
Adapted from Comfort Food Fix by Ellie Krieger
Makes 8 servings
INGREDIENTS
½ small red onion, thinly sliced into half-moons
¾ pound green beans, trimmed
¾ pound wax beans, trimmed
¼ cup honey
½ cup cider vinegar
3 tablespoons extra-virgin olive oil
½ teaspoon salt
¼ teaspoon freshly ground black pepper
1 15-ounce can no-salt-added kidney beans, rinsed and drained
1 medium red bell pepper, trimmed and sliced into matchsticks
DIRECTIONS
1. To mellow the bite of the onion, place it in a bowl of ice water and allow it to soak for 30 
minutes. Drain.
2. Place the green and wax beans in a steam basket fitted over a pot of boiling water. Cover 
and steam until crisp-tender, about 4 minutes. Remove from the heat and allow to cool. 
Cut into 2-inch lengths.
3. In a large bowl, whisk together the honey, vinegar, oil, salt, and black pepper. Add the 
onion, green and wax beans, kidney beans, and bell pepper and toss to combine. Cover and 
refrigerate for at least 1 hour before serving.
Per Serving: Calories 160; Fat 5 g; Sat Fat 1 g; Protein 5 g; Carbs 23 g; Fiber 7 g; Cholesterol 0 mg; Sodium 160 mg. 
11Autumn Vegetable Curry
Adapted from Comfort Food Fix by Ellie Krieger
Makes 6 servings
INGREDIENTS
1 large onion, coarsely chopped
4 cloves garlic, peeled
1 1½-inch length fresh ginger, peeled and thinly sliced
1½ tablespoons yellow curry powder
¼ teaspoon cayenne pepper, plus more to taste
2 tablespoons canola oil
2 tablespoons tomato paste
2 cups low-sodium vegetable broth
1 cup light coconut milk
1 cinnamon stick
¼ teaspoon freshly ground black pepper, plus more to taste
½ head cauliflower, broken into 1½-inch-wide florets  
(about 3 cups)
1 pound sweet potatoes, peeled and cut into 1-inch cubes
2 large carrots, peeled and cut into 1-inch rounds
2 tomatoes, cored and chopped
Grated zest of 1 lime
2 tablespoons fresh lime juice
1 15-ounce can no-salt-added chickpeas, drained and rinsed 
5 cups fresh baby spinach leaves
¾ teaspoon salt
¼ cup chopped fresh cilantro leaves
3 cups cooked brown rice, for serving, optional
DIRECTIONS
1. Place the onion, garlic, ginger, curry powder, and cayenne pepper in a food processor and 
process to combine. Add the oil and process until a smooth puree is formed. T ransfer the 
curry puree to a large pot and cook over medium heat, stirring frequently, about 5 minutes. 
Add the tomato paste and cook, stirring frequently, until the mixture begins to darken, 
about 5 minutes more.
2. Add the vegetable broth, coconut milk, cinnamon stick and ¼ teaspoon black pepper and 
bring to a boil. Reduce the heat and simmer for 10 minutes. Add the cauliflower, sweet 
potatoes, carrots, and tomatoes, season with salt and pepper, and return to a boil. Reduce 
the heat to medium low, cover, and simmer until the vegetables are tender, about 25 
minutes. Remove the cinnamon stick. Stir in the lime zest and juice, chickpeas, and spinach 
and cook until the spinach is wilted, about 5 minutes. Season with up to ¾ teaspoon salt.
3. Garnish with cilantro and serve with rice.
Per Serving: Calories 380; Fat 8 g; Sat Fat 2.5 g; Protein 11 g; Carbs 67 g; Fiber 11 g; Cholesterol 0 mg; Sodium 480 mg. 
 

12Honey-Crisp Oven-Fried Chicken
Adapted from Comfort Food Fix by Ellie Krieger
Makes 6 servings
INGREDIENTS
6 skinless, bone-in chicken thighs (about 2 pounds)
2/3 cup low-fat buttermilk
4 cups whole-grain cereal flakes
½ teaspoon paprika
½ teaspoon garlic powder
½ teaspoon kosher salt
¼ teaspoon freshly ground black pepper
¼ teaspoon cayenne pepper
Olive oil cooking spray
2 tablespoons honey
DIRECTIONS
1. Place the chicken in a bowl with the buttermilk and toss  
to coat. Marinate in the refrigerator for at least 1 hour and up to 4 hours. 
2. Place the cereal flakes in a food processor and process until crumbs form (you should have 
about 1 cup of crumbs). 
3. T ransfer to a shallow dish and mix in the paprika, garlic powder, salt, black pepper, and 
cayenne pepper.
4. Preheat the oven to 350°F . Spray a baking sheet with cooking spray. 
5. Remove chicken from buttermilk, shaking off excess buttermilk from the chicken. Discard 
the remaining buttermilk. 
6. Brush each piece of chicken with honey, then dip in the cereal crumbs, press hard so the 
crumbs adhere to the chicken. Place the coated chicken on the prepared baking sheet. 
7. Lightly spray the top of each chicken thigh with cooking spray. 
8. Bake until the chicken is crisped and cooked through, 45 to 50 minutes. 
Per Serving: Calories 330; Total Fat 7 g; Sat Fat 2 g; Protein 34 g; Carbs 34 g; Fiber 4 g; Cholesterol 125 mg; Sodium 410 mg.
 

13Apple Crisp
Adapted from Comfort Food Fix by Ellie Krieger
Makes 8 servings
INGREDIENTS FOR THE TOPPING
1/3 cup old-fashioned rolled oats
½ cup whole-wheat pastry flour
¼ cup sliced almonds
2 tablespoons toasted wheat germ
¼ cup packed dark brown sugar
¾ teaspoon ground cinnamon
¼ teaspoon ground nutmeg
1/8 teaspoon salt
1 tablespoon cold unsalted butter, cut into pieces
2 tablespoons canola oil
1 to 2 tablespoons cold water
INGREDIENTS FOR THE FILLING
3 large Rome or Empire apples (about 1½ pounds)
3 medium Golden Delicious apples (about 1 pound)
3 medium Granny Smith apples (about 1 pound)
¼ cup fresh lemon juice
3 tablespoons pure maple syrup
2 tablespoons whole wheat pastry flour
DIRECTIONS
1.  Preheat the oven to 375°F . 
2. To make the topping, place the oats, flour, almonds, wheat germ, brown sugar, cinnamon, 
nutmeg, and salt in a food processor and process until well combined. Add the butter and oil 
and pulse until lumps form. Add the water 1 tablespoon at a time until the dough just holds 
together when you press it between your fingers. T ransfer to a bowl and using your fingers, 
press the dough to create several pea-size lumps for texture. Chill until ready to use.
3. To make the filling, leaving the peels on, core and cut the apples into ¼-inch-thick wedges. 
Toss the wedges with the lemon juice and maple syrup until well coated. Sprinkle with the 
flour and toss until well combined. Spoon the apple mixture into a 3- to 3½-quart shallow 
baking dish and sprinkle the dough evenly over the top.
4. Bake in the middle of the oven until bubbling, the apples are tender, and the topping is 
golden brown, 45 to 50 minutes. 
Per Serving: Calories 280; Total Fat 7 g; Sat Fat 1.5 g; Protein 4 g; Carbs 53 g; Fiber 7 g; Cholesterol 5 mg; Sodium 40 mg. 
 

14EMERIL LAGASSE’S RECIPES FROM  
NEW ORLEANS
Tuscan Kale & White Bean Ragout 
Adapted from  From Farm to Fork  by Emeril Lagasse
Makes 4 servings
 
INGREDIENTS
2 tablespoons olive oil 
1 bay leaf 
2 cloves garlic, smashed and roughly chopped 
¼ teaspoon crushed red pepper 
1 small red onion, sliced 
1½ pounds T uscan kale,* rinsed, patted dry, and cut crosswise into 1-inch-wide slices 
¼ teaspoon freshly ground black pepper, plus more if needed 
2 15-ounce cans no-salt-added cannellini beans or white beans, drained and rinsed
1 cup canned no-salt-added diced tomatoes, with their juices 
½ cup vegetable stock or canned low-sodium vegetable broth 
½ teaspoon kosher salt
Extra-virgin olive oil, for drizzling 
DIRECTIONS
1. Heat the olive oil in a large sauté pan over medium-high heat. When it is hot, add the bay 
leaf, garlic, crushed red pepper, and red onion. Cook until the onion begins to wilt and the 
garlic begins to turn golden around the edges, 3 to 4 minutes. Add the kale and pepper, and 
cook for another 2 minutes. Then add the white beans, tomatoes, and stock. Cover, and 
cook until the kale is wilted and cooked through, about 15 minutes. Taste and season with 
up to ½ teaspoon salt. 
2. T ransfer the ragout to a serving dish, and drizzle it with extra-virgin olive oil. Serve hot. 
Per Serving: Calories 410; Fat 16 g; Sat Fat 2 g; Protein 17 g; Carbs 53 g; Fiber 13 g; Cholesterol 0 mg; Sodium 410 mg. 
*Tuscan kale is also known as lacinato kale, black kale, and dinosaur kale.
15Gumbo with Smoked Turkey & Wild Rice 
Adapted from  From Farm to Fork  by Emeril Lagasse
Makes 6 servings
INGREDIENTS
2 tablespoons olive oil
1 small onion, chopped 
3 tablespoons chopped scallions, white and light green parts, plus more for garnish 
½ tablespoon chopped garlic 
½ pound smoked turkey thigh or smoked turkey sausage, diced 
1½ pounds fresh cooking greens – a mix of spinach, collard greens, turnip greens -tough stems 
removed, leaves rinsed and coarsely chopped 
½ pound green cabbage, cored and coarsely chopped 
3 quarts chicken stock or canned low-sodium chicken broth 
2 cups wild rice 
2 or 3 small bay leaves 
¼ teaspoon cayenne pepper, more to taste 
Pinch of ground thyme 
¼ teaspoon kosher salt
1 tablespoon filé powder,* or more to thicken (optional) 
Chopped fresh parsley leaves, for garnish 
DIRECTIONS
1. Heat the oil in a large soup pot. Add the onion, scallions, and garlic, and cook until tender, 
about 3 minutes. Add the turkey and cook for 2 minutes. A handful at a time, add the 
spinach, collards, turnip greens, and cabbage, stirring them until wilted before adding the 
next bunch. Then add the stock, wild rice, bay leaves, cayenne, and thyme. Bring to a boil. 
Reduce the heat to a simmer and cook for 1 hour. 
2. Taste and add up to ¼ teaspoon salt—the greens should be tender and slightly spicy. The 
wild rice should be tender and puffed. 
3. If you wish to thicken it, stir 1 tablespoon filé powder into the simmering gumbo. Add 
more filé, a little at a time, until thickened. Simmer for 3 minutes more. (Do not allow the 
gumbo to boil once you have added the filé.) 
4. Serve garnished with chopped parsley and scallions. 
Per Serving: Calories 350; Fat 7 g; Sat Fat 1 g; Protein 21 g; Carbs 53 g; Fiber 9 g; Cholesterol 15 mg; Sodium 440 mg. 
*Filé powder is a spicy ground herb traditionally used to thicken and flavor gumbo.
16Braised Kohlrabi with Fennel & Leeks 
Adapted from  From Farm to Fork  by Emeril Lagasse
Makes 6 servings
INGREDIENTS
2 tablespoons olive oil 
1 tablespoon butter 
3 large heads kohlrabi, cut into ½-inch-thick wedges 
2 leeks, white and light green parts, well rinsed and sliced into ¼-inch-thick rounds 
1 large bulb fennel, cored and sliced 
¼ cup dry white wine 
1 cup vegetable stock, or canned low-sodium vegetable broth, more as needed
4 sprigs fresh thyme 
3 sprigs fresh fennel fronds, plus 1 tablespoon chopped 
¼ teaspoon freshly ground white pepper 
¼ teaspoon kosher salt 
DIRECTIONS
1. Combine the olive oil and butter in a large, deep sauté pan. Once the butter has melted 
and the foam has subsided, add the kohlrabi, leeks, and fennel. Cook for 4 to 5 minutes, 
browning the kohlrabi on both sides. Add the wine and cook until it has reduced by half. 
Then add the vegetable stock, thyme, and fennel fronds, and season with the pepper. Cook, 
partially covered, for 20 minutes, or until the vegetables are crisp-tender. 
2. Remove the thyme sprigs. Serve the vegetables in a shallow bowl with some of the braising 
liquid, garnished with the chopped fennel fronds. Season with up to ¼ teaspoon salt.
Per Serving: Calories 110; Fat 5 g; Sat Fat 1 g; Protein 2 g; Carbs 12  g; Fiber 5 g; Cholesterol 0 mg; Sodium 140 mg.
17LYNNE ROSSETTO KASPER’S RECIPES  
Rosemary-Orange Cauliflower Puree
Adapted from How to Eat Weekends by Lynne Rosetto Kasper
Makes 8 servings
INGREDIENTS
1 large cauliflower (2½ to 3 pounds) with its greens
¼ pound T uscan kale* (about 6 leaves) or regular kale, ribs removed and leaves torn
1 large onion, thinly sliced
6 garlic cloves, crushed
1½ tightly packed teaspoons fresh rosemary leaves, or more to taste
Finely grated zest of 2/3 large orange, or to taste
freshly ground black pepper
½ teaspoon salt
¼ cup extra-virgin olive oil
1 tablespoon unsalted butter
DIRECTIONS
1. Cut the cauliflower into florets, then thinly slice the green stalks.
2. Place 3 inches water in an 8-quart pot. Insert a collapsible steamer. Bring the water to a 
boil and pile in the cauliflower greens, then the florets then add the kale, onion, garlic, 
rosemary, and orange zest. Sprinkle with some pepper.
3. Steam for about 10 minutes, or until the cauliflower is almost falling apart. Drain in a 
colander and let stand for 5 minutes. Place everything into a food processor along with ¼ 
teaspoon salt, the oil and butter. Purée, then taste for additional seasoning, be it salt (up to 
another ¼ teaspoon), rosemary, orange zest, or pepper.
Per Serving: Calories 130; Fat 9 g; Sat Fat 2 g; Protein 4 g; Carbs 11 g; Fiber 3 g; Cholesterol 5 mg; Sodium 170 mg. 
*Tuscan kale is also known as lacinato kale, black kale, and dinosaur kale.
18Pomegranate-Cinnamon Tabbouleh
Adapted from How to Eat Weekends by Lynne Rosetto Kasper
Makes 6 servings
GRAIN
1½ cups medium or coarsely ground bulgur wheat
DRESSING
1 large garlic clove, minced
Generous ¼ teaspoon ground cinnamon
3 tablespoons pomegranate molasses*
2 to 3 tablespoons water or dry white wine
¾ teaspoon salt
Freshly ground black pepper
1/3 cup expeller-pressed canola or safflower oil
SALAD
2 Belgian endives or ½ medium head of radicchio, trimmed, cored, and coarsely chopped
1 medium fennel bulb, cored, quartered, and coarsely chopped, fronds reserved
½ cup chopped fresh flat-leaf parsley
2 tightly packed tablespoons fresh mint, coarsely chopped
2 to 3 scallions (white parts only), thinly sliced
¼ cup shelled, salted pistachios, coarsely chopped
Seeds from 1 large pomegranate, white membrane removed
Salt and freshly ground black pepper
DIRECTIONS
1. Soak the bulgur: Place the bulgur in a bowl and add boiling water to cover by 2 inches. 
Soak for 10 to 20 minutes, depending on the grind of the grain. Taste for tenderness, but 
be sure it’s not mushy. Drain well, squeezing out as much extra moisture as possible by 
wrapping the grain in a clean towel and wringing it out. If time allows, spread out the 
bulgur on a fresh towel to help it dry a bit. T ransfer the bulgur to a large bowl.
2. Make the dressing: In a medium bowl, combine the garlic, cinnamon, pomegranate 
molasses, water, salt, and pepper to taste. Stir well. Add the oil in a slow stream while 
whisking until emulsified.
3. Make the salad: Toss into the bulgur the endive, fennel, parsley, mint, scallions, and 
pistachios. Gently fold in the pomegranate seeds and the dressing. Taste for seasoning and 
add up to another ¼ teaspoon salt and pepper to taste.  Garnish with the fennel fronds, and 
serve.
Per Serving: Calories 220; Fat 8 g; Sat Fat 0.5 g; Protein 6 g; Carbs 36 g; Fiber 8 g; Cholesterol 0 mg; Sodium 260 mg. 
*Pomegranate molasses substitute: simmer 1 cup pomegranate juice and 1 tablespoon fresh lemon juice  until reduced to 3 tablespoons.
19KATE SHERWOOD’S  
AUTUMN RECIPES 
Lentil, Apple & Walnut Salad with  
Cider Dressing
by Kate Sherwood
Makes 8 servings
INGREDIENTS
1½ cups French lentils
3 cloves garlic
2 sprigs thyme
1 bay leaf
2 cups apple cider
2 tablespoons whole grain Dijon mustard
2 tablespoons cider vinegar
2 shallots, minced
3 tablespoons canola oil
½ teaspoon kosher salt
Freshly ground black pepper
1 apple, diced
5 ounces baby spinach
½ cup chopped walnuts
DIRECTIONS
1. In a medium pot, cover the lentils, garlic, thyme and bay leaf with water by 2 inches.  
2. Bring to a boil then reduce to a simmer.  Cook until tender but not mushy – start checking 
them at 15 minutes. 
3. Drain, rinse under cold water and discard the garlic, thyme and bay leaf. 
4. In a sauté pan, boil the cider until reduced to 1/3 cup. Allow to the cider to cool then whisk 
reduced cider together with the mustard, vinegar, shallots, and oil.  
5. Season the dressing with up to ½ teaspoon salt and pepper. Toss apples, lentils and spinach 
in the dressing.  Arrange salad on a platter and garnish with the walnuts.  
Per Serving: Calories 260; Total Fat 10 g; Sat Fat 0.5 g; Protein 12 g; Carbs 32 g; Fiber 10 g; Cholesterol 0 mg; Sodium 240 mg. 

20Pearl Barley with Spinach Pesto 
by Kate Sherwood 
Makes 8 servings 
INGREDIENTS
1½ cups pearl barley
1 clove garlic
¼ cup pine nuts, toasted
½ cup grated parmesan
4 cups baby spinach
¼ cup extra-virgin olive oil
¾ teaspoon kosher salt
¼ teaspoon freshly ground black pepper
1 cup edamame
DIRECTIONS
1. Boil the barley in plenty of water until al dente (chewy but not raw in the center), about 30 
minutes. While the barley is cooking, make the pesto.  
2. Pulse the garlic, pine nuts, cheese, spinach, oil, salt and pepper in a food processor until 
finely chopped. 
3. Reserve ½ cup cooking water.  
4. Toss the edamame into the pot with the barley then drain and return them to pot.  
5. Stir ¼ cup of cooking water into the pesto.  
6. Stir the pesto into the barley and edamame.  Add more water if needed to loosen.  
Per Serving: Calories 260; Total Fat 12 g; Sat Fat 2.5 g; Protein 7 g; Carbs 32 g; Fiber 6 g; Cholesterol 5 mg; Sodium 280 mg. 
21Yogurt Panna Cotta with Cranberry  
Pear Sauce 
by Kate Sherwood
Makes 8 servings
PANNA COTTA* INGREDIENTS
1 cup low-fat (1%) milk
¼ cup sugar
1 envelope plain powdered gelatin
2 tablespoons cold water
1 large container (16-18 ounces) fat-free Greek yogurt
1 teaspoon pure vanilla extract
1 recipe cranberry pear sauce (see below)
DIRECTIONS
1. In a large saucepan, heat the milk with the sugar over  
low heat, stirring, until the sugar has dissolved,  
about 3 minutes. Remove fromt he heat.
2. Meanwhile, in a small bowl, mix the gelatin with the water and let stand for 2 minutes. 
3. Whisk the gelatin into the warm milk and let cool.
4. In a medium bowl, whisk together the yogurt and vanilla extract. Whisk in the milk. 
5. Pour 1/3 cup of the mixture into each of 8 serving glasses. 
6. Refrigerate until set, about 2 hours. Serve with the cranberry pear sauce.  
SAUCE INGREDIENTS
1 cup fresh or frozen cranberries
2 ripe pears, pealed, cored and diced
¼ cup sugar
1 cup water
DIRECTIONS
1. Combine all the ingredients in a sauce pan and bring to a boil. Reduce the heat and simmer 
for 20 minutes.  
2. T ransfer to a heat-proof bowl and cool to room temperature, about 1 hour.
Per Serving: Calories 120; Total Fat 0 g; Sat Fat 0 g; Protein 7 g; Carbs 32 g; Fiber 2 g; Cholesterol 0 mg; Sodium 40 mg. 
*Frozen vanilla yogurt can be substituted for the panna cotta recipe (as pictured).

22VEGETARIAN RECIPES FROM  
MARIE SIMMONS
Carrot, Sweet Potato & Ginger Soup 
Adapted from Fresh and Fast Vegetarian  by Marie Simmons
Makes about 10 cups
INGREDIENTS
2 tablespoons extra-virgin olive oil
1 pound carrots, cut into ½-inch slices
1 pound sweet potatoes, scrubbed, skins left on, cut into ½-inch cubes
1 bunch scallions (white and green parts), sliced
½ cup chopped celery
1 garlic clove, grated
1 tablespoon chopped peeled fresh ginger
1 teaspoon coarse salt
4 tablespoons chopped fresh cilantro
1 tablespoon fresh lime juice
1 tablespoon finely chopped seeded jalapeño pepper, or to taste
6 ounces baby bok choy, stem ends trimmed, cut into ½-inch slices
DIRECTIONS
1. Heat the oil in a soup pot until it is hot enough to sizzle a piece of vegetable. Add the 
carrots, sweet potatoes, scallions, celery, garlic, ginger, and ½ teaspoon salt. Cook, covered, 
stirring occasionally, over medium-low heat until lightly browned and softened, about 10 
minutes. Add 6 cups water and 2 tablespoons of the cilantro and bring to a boil. Cover and 
cook over medium heat until the vegetables are tender, 20 to 25 minutes.
2. Ladle out about 2 cups of the solid vegetables and set aside. Use an immersion blender to 
puree the soup in the pot. If you don’t have an immersion blender, let the soup cool slightly, 
transfer it to a blender or food processor, in batches if necessary, and puree until smooth. 
Return the soup to the pot.
3. Add the reserved vegetables, lime juice, and jalapeño. Bring the soup to a boil. Stir in the 
bok choy and cook for 30 seconds. Taste and season with up 1/2 teaspoon salt. Ladle the 
soup into bowls and garnish with the remaining 2 tablespoons chopped cilantro.
Per  Serving (1 cup): Calories 90; Total Fat 3 g; Sat Fat 0 g; Protein 2 g; Carbs 15 g; Fiber 3 g; Cholesterol 0 mg; Sodium 270 mg. 
 
23Shredded Tuscan Kale, Tomato &  
Avocado Salad
Adapted from Fresh and Fast Vegetarian  by Marie Simmons
Makes 4 servings
SALAD
1 small bunch (about 10 ounces) T uscan kale,* washed and dried
2 tablespoons fresh lime juice
1 tablespoon extra-virgin olive oil
1/8 teaspoon coarse salt
SALSA
1 avocado, halved, pitted, peeled and cut into ¼-inch dice
1 ripe tomato, cut into ¼-inch dice with seeds and juice
½ cup diced (¼ inch) red onion
1 teaspoon finely chopped seeded jalapeño pepper, plus more to taste
1 small garlic clove, grated
1 tablespoon lime juice
1 tablespoon extra-virgin olive oil
¼ teaspoon coarse salt
¼ cup unsalted roasted pepitas (pumpkin seeds) or roasted sunflower seeds
DIRECTIONS
1. To prepare the kale, cut along both sides of the stem of each leaf with a sharp knife or pull 
the ruffled leaves away from the stems with your hands. Discard the stems. Gather a bunch 
of the long kale leaves together on the cutting board and slice into thin (¹⁄8-inch) crosswise 
slices. You should have 4 to 6 cups lightly packed.
2. Combine the kale, lime juice, oil, and salt in a large bowl. Rub the ingredients together 
with your hands (as though giving the kale a massage) until the leaves wilt, 1 to 2 minutes. 
Set aside.
3. To make the salsa: Combine the avocado, tomato, red onion, jalapeño, garlic, lime juice, 
oil, and salt and stir to blend.
4. Add the salsa to the kale and toss to combine. Sprinkle the salad with the pepitas. Serve at 
room temperature.
Per Serving: Calories 240; Total Fat 19 g; Sat Fat 3 g; Protein 6 g; Carbs 16 g; Fiber 6 g; Cholesterol 0 mg; Sodium 220 mg. 
*Tuscan kale is also known as lacinato kale, black kale, and dinosaur kale.
24Curried Lentils with Walnuts, Spinach & Cherry Tomatoes 
Adapted from Fresh and Fast Vegetarian  by Marie Simmons
Makes 4 servings
INGREDIENTS
1 cup brown lentils
2 tablespoons extra-virgin olive oil
1 cup chopped onion
2 teaspoons curry powder
1 garlic clove, grated
2 bags (5–6 ounces each) baby spinach (8–10 cups packed), rinsed and drained
1 cup small cherry or grape tomatoes, stems removed
2 tablespoons finely chopped fresh mint
½ cup chopped walnuts
½ cup plain yogurt
DIRECTIONS
1. Bring a medium saucepan half full of water to a boil. Add the lentils and cook, uncovered, 
until tender but not mushy, 18 to 20 minutes. Drain and set aside.
2. Heat the oil in a large skillet until hot enough to sizzle a piece of onion. Add the onion 
and cook, stirring, until tender, about 5 minutes. Add the curry powder and garlic and 
cook, stirring, for 1 minute. Add the cooked lentils, spinach, tomatoes and mint and cook, 
stirring, until heated through, about 5 minutes.
3. Meanwhile, heat the walnuts in a small skillet over medium heat, stirring, until toasted, 
about 5 minutes. Sprinkle the walnuts over the lentils and serve with the yogurt to spoon 
over the top.
Per Serving: Calories 400; Total Fat 17 g; Sat Fat 2 g; Protein 18 g; Carbs 47 g; Fiber 20 g; Cholesterol 0 mg; Sodium 150 mg. 
 
25Oven-Roasted Stuffed Portobello Mushrooms
Adapted from Fresh and Fast Vegetarian  by Marie Simmons
Makes 4 servings
INGREDIENTS
4 large Portobello mushrooms, wiped clean, stems removed and reserved
4 tablespoons extra-virgin olive oil
½ cup chopped onion
1 cup coarse bread crumbs from lightly toasted whole wheat bread
2 tablespoons finely chopped fresh Italian parsley
2 tablespoons oil-packed sun-dried tomatoes, drained, blotted dry, and chopped
1 garlic clove, grated
¼ teaspoon coarse salt 
Freshly ground black pepper
DIRECTIONS
1. Preheat the oven to 400°F . Finely chop the mushroom stems.
2. Meanwhile, heat 2 tablespoons of the oil in a medium skillet until it is hot enough to 
sizzle a piece of onion. Add the onion and chopped mushroom stems and cook, stirring, 
over medium heat until golden, about 5 minutes. Add the bread crumbs, parsley, sun-
dried tomatoes and garlic and cook, stirring, until the crumbs are heated through, about 2 
minutes. Sprinkle with salt and pepper to taste and set aside.
3. Brush the tops and bottoms of the mushroom caps with the remaining 2 tablespoons oil. 
Sprinkle on both sides with a pinch salt and a grinding of black pepper. Place on a baking 
sheet, rounded sides up, add ¼ cup water and roast for 10 minutes.
4. Remove the pan from the oven. T urn the caps over, fill with the crumb mixture, dividing it 
evenly, and roast until browned and crisp, about 10 minutes more. T ransfer to a platter and 
serve.
Per Serving: Calories 190; Total Fat 15 g; Sat Fat 2 g; Protein 3 g; Carbs 12 g; Fiber 2 g; Cholesterol 0 mg; Sodium 200 mg. 
26ASIAN RECIPES FROM  
NINA SIMONDS
Hot & Sour Salmon with Greens
Adapted from A Spoonful of Ginger  by Nina Simonds
Makes 6 servings
INGREDIENTS
2½ pounds baby bok choy or bok choy, stem ends and leaf  
tips trimmed
8 whole scallions, ends trimmed, cut into thin slices  
on the diagonal
¼ cup fresh ginger cut into very thin julienne shreds
6 salmon steaks, about 6 ounces each
3 cups cooked brown rice
DRESSING
3 tablespoons reduced-sodium soy sauce
2 tablespoons Chinese black vinegar or balsamic vinegar
2 tablespoons sugar
1 tablespoon minced garlic
DIRECTIONS
1. T rim the tough outer leaves from the bok choy and discard. Rinse the stalks and leaves and 
drain.  Cut the stalks in half lengthwise.  Cut the halves diagonally into 2-inch sections.  In 
a bowl, toss the scallions and ginger with the bok choy sections.  Arrange on a heatproof 
platter. 
2. Mix the ingredients of the dressing and pour into a serving bowl.
3. Preheat the oven to 450°F . Place the salmon steaks on top of the greens. Pour into a 
roasting pan several inches of water and heat until boiling. Carefully place the platter of 
salmon and vegetables on top of a rack or steamer tray in the roasting pan.  Cover the top 
of the pan tightly with aluminum foil.  Bake 7 to 9 minutes, or until the fish is cooked.  
4. Serve the salmon from the heat-proof platter or arrange the steamed vegetables and salmon 
on serving plates.  Spoon the dressing on top and serve with brown rice. 
Per Serving: Calories 430; Total Fat 14 g; Sat Fat 2 g; Protein 44 g; Carbs 32 g; Fiber 4 g; Cholesterol 105 mg; Sodium 480 mg. 
 

27Spicy Garlic Broccoli with Pine Nuts
Adapted from A Spoonful of Ginger  by Nina Simonds
Makes 6 servings
INGREDIENTS
1½ pounds broccoli
¼ cup pine nuts
1½ teaspoons canola or corn oil
1½ teaspoons toasted sesame oil
1 teaspoon hot chili paste or ¾ teaspoon crushed dried chilies
2 tablespoons minced garlic
2½ tablespoons rice wine or sake, mixed with 2 tablespoons water
SAUCE (MIXED TOGETHER IN A BOWL UNTIL THE SUGAR IS DISSOLVED)
1 tablespoon reduced sodium-soy sauce
1 teaspoon sugar
DIRECTIONS
1. T rim the ends of the broccoli, separate the florets, peel the outer skin of the stem and cut it 
on the diagonal into 1-inch lengths. 
2. Toast the pine nuts until golden in a 300°F oven, turning them occasionally so that they 
cook evenly for about 20 minutes. 
3. Heat a wok or large skillet, add the oils, and heat until hot, about 20 seconds. Add the chili 
paste or crushed chilies and garlic, and stir-fry, tossing with a slotted spoon over medium 
heat until fragrant, about 15 seconds. T urn the heat to high. 
4. Add the stem sections of the broccoli and stir-fry.  Pour in the rice wine and water and 
cook, tossing, about 30 seconds, then cover and cook about 1½ to 2 minutes, until the 
stems are just tender. Add the florets and toss over high heat, cooking for about 1½ minutes 
or until just tender.  
5. Add the premixed sauce and toss lightly for 15 seconds. Add the toasted pine nuts and stir-
fry a few seconds to combine the ingredients. Scoop the ingredients into a serving bowl and 
serve immediately. 
Per Serving: Calories 90; Total Fat 6 g; Sat Fat 1 g; Protein 4 g; Carbs 8 g; Fiber 4 g; Cholesterol 0 mg; Sodium 125 mg. 
28Rainbow Salad with Spicy Peanut Dressing
Adapted from A Spoonful of Ginger  by Nina Simonds
Makes 6 servings
INGREDIENTS
14 ounces firm tofu, cut into ½ inch slabs
½ pound whole wheat spaghetti
1 teaspoon toasted sesame oil
2 cups grated carrots
1½ cups grated cucumbers, seeds and skin removed
1½ cups grated red cabbage
1 red bell pepper, cored, seeded, and sliced into thin strips
1 yellow pepper, cored seeded, and sliced into thin strips
SPICY PEANUT DRESSING
2 tablespoons minced fresh ginger
½ tablespoon minced garlic
1 teaspoon hot chili paste, or more to taste
½ cup smooth peanut butter
¼ cup reduced-sodium soy sauce
1 tablespoon sugar
2 tablespoons Chinese black vinegar or balsamic vinegar
3 tablespoons toasted sesame oil
¼ cup water
DIRECTIONS
1. Wrap the tofu slabs in paper towels or a cotton towel and place a heavy weight, such as a 
cast-iron skillet, on top. Let stand for 30 minutes to press out the excess water, then cut the 
tofu into matchstick-size shreds about 2 inches long. 
2. Bring 3 quarts water to a boil, add the spaghetti, and cook until just tender. Drain in a 
colander, toss with the sesame oil, and arrange on a platter. 
3. Arrange the carrots, cucumbers, bean sprouts, red and yellow pepper strips, and tofu in 
mounds or separate concentric circles on the serving platter with the noodles. 
4. To prepare the Spicy Peanut Dressing: In a food processor fitted with a steel blade or a 
blender, chop the ginger and garlic until fine. Add the remaining ingredients in descending 
order, ending with the water. Process until smooth. The sauce should have the consistency 
of heavy cream. If it is too thick, add more water; if too thin, add more peanut butter. Pour 
the sauce into a serving container, and offer the vegetables and sauce to each diner to mix as 
desired. 
Per Serving: Calories 430; Total Fat 21 g; Sat Fat 3.5 g; Protein 18 g; Carbs 46 g; Fiber 9 g; Cholesterol 0 mg; Sodium 530 mg. 
</document_content>

<question>
what are the ingredients for Quick Tostados? 
</question>
"""
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "<thinking>"
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0.1,
                "maxTokens": 5000,
                "stopSequences": ["</answer>"]
            }
            )

print(json.dumps(response, indent=2))