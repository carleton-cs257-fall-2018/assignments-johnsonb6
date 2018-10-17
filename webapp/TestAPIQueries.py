import unittest

class TestAPIQueries(unittest.TestCase):

    def test_base_depth_query(self):
        date = "get a date from table"
        base_depth_from_API = get_base_depth(date)
        base_depth_from_data = "hard coded base depth from date above"
        self.assertEqual(base_depth_from_API, base_depth_from_data)

    def test_snowfall_query(self):
        date = "get a date from table"
        snowfall_from_API = get_snowfall(date)
        snowfall_from_data = "hard coded snowfall from date above"
        self.assertEqual(snowfall_from_API, snowfall_from_data)

    def test_forecast(self):
        start_date = "get a date from table"
        end_date = "get a date from table"
        multiple_day_snowfall_from_API = get_multiple_day_snowfall(start_date, end_date)
        multiple_day_snowfall_from_data = "hard coded snowfall from dates above"
        self.assertEqual(multiple_day_snowfall_from_API, multiple_day_snowfall_from_data)

    def test_base_depth_graph(self):
        start_date = "get a date from table"
        end_date = "get a date from table"
        multiple_day_base_depth_from_API = get_multiple_day_base_depth(start_date, end_date)
        multiple_day_base_depth_from_data = "hard coded base depth from dates above"
        self.assertEqual(multiple_day_base_depth_from_API, multiple_day_base_depth_from_data)

    def test_date_query(self):
        date_from_data = "day with most snowfall of X year"
        date_from_API = get_day_with_most_snowfall(year)
        self.assertEqual(date_from_data, date_from_API)


if __name__ == "__main__":
    unittest.main()
