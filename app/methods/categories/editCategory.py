from app.models.Category import Category
from app import db
from app.methods.restaurants import isExistedRestaurant
# Dish = models.Dish.Dish
# Category = models.Category.Category
# Ingredient = models.Ingredient.Ingredient

def editCategory(category):
    errors = {}
    category_info = category

    if "id" not in category:
        errors["id"] = "NOT_EXISTED"

    if "restaurant_id" not in category:
        errors["restaurant_id"] = "NOT_EXISTED"
    else:
        if isExistedRestaurant(category["restaurant_id"]) == False:
            errors["restaurant_id"] = "NOT_EXISTED_RESTAURANT_ID"

    if errors == {}:
        categoryGet = db.session.query(Category).filter(
            (Category.id == category["id"]) &
            (Category.restaurant_id == category["restaurant_id"])
        ).first()
        # category = Category.create(category)

        if categoryGet != None:
            categoryGet.edit(category)
            category_info = categoryGet.getInfo()
        else:
            errors["main"] = "NOT_EXISTED"
            category_info = category

            # if logo_flag:
            #     path = fileSave(logo, 'restaurant', f'{restaurant.id}.png')
            #     restaurant.setLogo(path)
        #
        # except:
        #     errors["main"] = category["error"]
        #     category_info = category["category"]

    # try:
    #     category_title = category["category_title"]
    # except:
    #     return {"error": "add-dish: category_title not exists"}



    # if category == None:
    #     return {"error": "add-dish: Category not found. Create category and try again."}

    return {"category": category_info, "errors": errors}