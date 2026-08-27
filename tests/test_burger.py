import pytest
from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_init(self): 

        burger = Burger()

        assert (burger.bun, burger.ingredients) == (None, [])

    def test_set_buns(self): 

        mock_bun = Mock()

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun


    def test_add_one_ingredient(self): 

        mock_ingredient = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]


    def test_add_some_ingredients(self): 
    
        first_mock_ingredient = Mock()
        second_mock_ingredient = Mock()
    
        burger = Burger()
        burger.add_ingredient(first_mock_ingredient)
        burger.add_ingredient(second_mock_ingredient)
        
        assert burger.ingredients == [first_mock_ingredient, second_mock_ingredient]


    def test_remove_all_ingredients_consistently(self): 
    
            first_mock_ingredient = Mock()
            second_mock_ingredient = Mock()
    
            burger = Burger()
            burger.add_ingredient(first_mock_ingredient)
            burger.add_ingredient(second_mock_ingredient)
    
            burger.remove_ingredient(1)
            burger.remove_ingredient(0)
    
            assert burger.ingredients == []


    def test_remove_ingredient_from_middle(self): 

        first_mock_ingredient = Mock()
        second_mock_ingredient = Mock()
        third_mock_ingredient = Mock()

        burger = Burger()
        burger.add_ingredient(first_mock_ingredient)
        burger.add_ingredient(second_mock_ingredient)
        burger.add_ingredient(third_mock_ingredient)

        burger.remove_ingredient(1)

        assert burger.ingredients == [first_mock_ingredient, third_mock_ingredient]


    @pytest.mark.parametrize('ingredient_current_position, ingredient_new_position, expected_ingredients_positions', 
                            [(0, 1, [1, 0, 2]), 
                             (1, 0, [1, 0, 2]), 
                             (0, 2, [1, 2, 0]), 
                             (2, 0, [2, 0, 1])])       
    def test_move_ingredients(self, ingredient_current_position, ingredient_new_position, expected_ingredients_positions):

        first_mock_ingredient = Mock()
        second_mock_ingredient = Mock()
        third_mock_ingredient = Mock()

        ingredients = [first_mock_ingredient, second_mock_ingredient, third_mock_ingredient]

        burger = Burger()
        burger.add_ingredient(first_mock_ingredient)
        burger.add_ingredient(second_mock_ingredient)
        burger.add_ingredient(third_mock_ingredient)

        burger.move_ingredient(ingredient_current_position, ingredient_new_position)

        expected_ingredients_list = []

        for index in expected_ingredients_positions:
            expected_ingredients_list.append(ingredients[index])
        
        assert burger.ingredients == expected_ingredients_list


    def test_get_price_burger_with_one_ingredient(self):

        mock_bun = Mock()
        mock_bun.get_price.return_value = 50.0

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_price.return_value = 200.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)

        assert burger.get_price() == 300.0


    def test_get_price_burger_with_two_ingredients(self):
    
        mock_bun = Mock()
        mock_bun.get_price.return_value = 50.0
    
        mock_first_ingredient = Mock()
        mock_first_ingredient.get_price.return_value = 200.0
    
        mock_second_ingredient = Mock()
        mock_second_ingredient.get_price.return_value = 50.0
    
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
    
        assert burger.get_price() == 350.0


    def test_get_price_burger_without_ingredients(self):
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 50.0
        
        burger = Burger()
        burger.set_buns(mock_bun)
        
        assert burger.get_price() == 100.0
            

    def test_get_receipt_for_burger_with_one_ingredient(self):

        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Tasty_bun'
        mock_bun.get_price.return_value = 100.0

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_name.return_value = 'Cheese_sauce'
        mock_first_ingredient.get_price.return_value = 50.0
        mock_first_ingredient.get_type.return_value = 'SAUCE'

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)

        expected_receipt = (
            "(==== Tasty_bun ====)\n"
            "= sauce Cheese_sauce =\n"  
            "(==== Tasty_bun ====)\n"
            "\n"
            "Price: 250.0"
        )

        assert burger.get_receipt() == expected_receipt


    def test_get_receipt_for_burger_with_two_ingredients(self):
    
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Tasty_bun'
        mock_bun.get_price.return_value = 100.0
    
        mock_first_ingredient = Mock()
        mock_first_ingredient.get_name.return_value = 'Chiken_stripes'
        mock_first_ingredient.get_price.return_value = 200.0
        mock_first_ingredient.get_type.return_value = 'FILLING'
    
        mock_second_ingredient = Mock()
        mock_second_ingredient.get_name.return_value = 'Cheese_sauce'
        mock_second_ingredient.get_price.return_value = 50.0
        mock_second_ingredient.get_type.return_value = 'SAUCE'
    
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
    
        expected_receipt = (
            "(==== Tasty_bun ====)\n"
            "= filling Chiken_stripes =\n"  
            "= sauce Cheese_sauce =\n"  
            "(==== Tasty_bun ====)\n"
            "\n"
            "Price: 450.0"
        )
    
        assert burger.get_receipt() == expected_receipt    


    def test_get_receipt_for_burger_without_ingredients(self):
    
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Tasty_bun'
        mock_bun.get_price.return_value = 100.0
    
        burger = Burger()
        burger.set_buns(mock_bun)
    
        expected_receipt = (
            "(==== Tasty_bun ====)\n"  
            "(==== Tasty_bun ====)\n"
            "\n"
            "Price: 200.0"
        )
    
        assert burger.get_receipt() == expected_receipt         