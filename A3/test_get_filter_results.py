import unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    '''Your unittests here'''
    """unittest test methods for get_filter_results."""


    def test_empty_query(self):
        """Test get_filter_results with twitterverse, list of str users 
        and empty filter dictionary."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['a', 'b', 'c', 'd']
        
        self.assertEqual(expected, actual)
    
    
    def test_empty_users(self):
        """Test get_filter_results with twitterverse, empty list of str users 
        and filter dictionary."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = []
        
        filter_dict = {'name-includes': 'r', 'location-includes':'E', 
                       'follower':'d', 'following':'a'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = []
        
        self.assertEqual(expected, actual)


    def test_filters_are_additive(self):
        """ Test that each filter step is applied to the list that resulted 
        from the previous filter step."""        
        
        twitterverse = {'a':{'name':'Andy', 'location':'China', 'web':'', 
                            'bio':'', 'following':[]},
                        'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                            'bio':'', 'following':['a']},
                        'c':{'name':'Charles', 'location':'England', 'web':'',
                            'bio':'', 'following':['a', 'b']},
                        'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                            'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
               
        filter_dict = {'name-includes':'e', 'location-includes': 'd', 
                       'following': 'c', 'follower': 'b'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = []
        
        self.assertEqual(expected, actual)         
        
        
    def test_name_includes_capital(self):
        """Test get_filter_results with twitterverse,list of str users, and 
        filter dictionary where only operation is name_includes with only 
        capital letters."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {'name-includes':'AN'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['a']
        
        self.assertEqual(expected, actual)
    
    
    def test_name_includes_lower(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is name_includes with only 
        lower-case letters."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {'name-includes':'ak'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['d']
        
        self.assertEqual(expected, actual)


    def test_name_includes_empty_keyvalue(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is name_includes with value 
        empty str."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {'name-includes':''}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['a', 'b', 'c', 'd']
        
        self.assertEqual(expected, actual)  
        
        
    def test_location_includes_capital(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is location_includes with only 
        capital letters."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'Yarts', 'web':'', 
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {'location-includes':'YA'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['c']
        
        self.assertEqual(expected, actual)
        

    def test_location_includes_lower(self):
        """Test get_filter_results with twitterverse, list of str users, and
        filter dictionary where only operation is location_includes with only
        lower-case letters."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {'location-includes':'en'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['c', 'd']
        
        self.assertEqual(expected, actual)


    def test_location_includes_empty_keyvalue(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is location_includes with value 
        empty str."""
        
        twitterverse = { 'a':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'b':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['a']},
                         'c':{'name':'Charles', 'location':'England', 'web':'',
                              'bio':'', 'following':['a', 'b']},
                         'd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                              'bio':'', 'following':['a', 'b', 'c']}}
        
        users = ['a', 'b', 'c', 'd']
        
        filter_dict = {'location-includes':''}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['a', 'b', 'c', 'd']
        
        self.assertEqual(expected, actual)
        
        
    def test_follower_operation_lower(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is follower with only lower-case
        letters."""
        
        twitterverse = { 'aa':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'bb':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['aa']},
                         'cc':{'name':'Charles', 'location':'England', 
                               'web':'','bio':'', 'following':['aa', 'bb']},
                         'dd':{'name':'Drake', 'location':'Denmark', 'web':'',
                              'bio':'', 'following':['aa', 'bb', 'cc']}}
        
        users = ['aa', 'bb', 'cc', 'dd']
        
        filter_dict = {'follower': 'cc'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['aa', 'bb']
        
        self.assertEqual(expected, actual)   
    
        
    def test_follower_operation_capital(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is following with capital 
        letters."""
                   
        twitterverse = {'AA':{'name':'Andy', 'location':'China', 'web':'', 
                            'bio':'', 'following':['aa']},
                        'aa':{'name':'Andy', 'location':'China', 'web':'', 
                            'bio':'', 'following':[]},                        
                        'bb':{'name':'Bert', 'location':'Germany', 'web':'', 
                            'bio':'', 'following':['AA', 'aa']},
                        'cc':{'name':'Charles', 'location':'England', 'web':'',
                            'bio':'', 'following':['AA', 'aa', 'bb']},
                        'dd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                            'bio':'', 'following':['AA', 'bb', 'cc']}}
    
        users = ['aa', 'bb', 'cc', 'dd']
                   
        filter_dict = {'follower': 'AA'}
                   
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
                   
        expected = ['aa']
                   
        self.assertEqual(expected, actual)
        
    
    def test_following_operation_lower(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is following with only 
        lower-case letters."""
        
        twitterverse = { 'aa':{'name':'Andy', 'location':'China', 'web':'', 
                              'bio':'', 'following':[]},
                         'bb':{'name':'Bert', 'location':'Germany', 'web':'', 
                              'bio':'', 'following':['aa']},
                         'cc':{'name':'Charles', 'location':'England', 
                               'web':'', 'bio':'', 'following':['aa', 'bb']},
                         'dd':{'name':'Drake', 'location':'Denmark', 'web':'',
                              'bio':'', 'following':['aa', 'bb', 'cc']}}
        
        users = ['aa', 'bb', 'cc', 'dd']
        
        filter_dict = {'following': 'cc'}
        
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
        
        expected = ['dd']
        
        self.assertEqual(expected, actual)    
    
    
    def test_following_operation_capital(self):
        """Test get_filter_results with twitterverse, list of str users, and 
        filter dictionary where only operation is following with only capital 
        letters."""
               
        twitterverse = {'AA':{'name':'Andy', 'location':'China', 'web':'', 
                            'bio':'', 'following':[]},
                        'aa':{'name':'Andy', 'location':'China', 'web':'', 
                            'bio':'', 'following':[]},                        
                        'bb':{'name':'Bert', 'location':'Germany', 'web':'', 
                            'bio':'', 'following':['AA', 'aa']},
                        'cc':{'name':'Charles', 'location':'England', 'web':'',
                            'bio':'', 'following':['AA', 'aa', 'bb']},
                        'dd':{'name':'Drake', 'location':'Denmark', 'web':'', 
                            'bio':'', 'following':['AA', 'bb', 'cc']}}
               
        users = ['bb', 'cc', 'dd']
               
        filter_dict = {'following': 'AA'}
               
        actual = tf.get_filter_results(twitterverse, users, filter_dict)
               
        expected = ['bb', 'cc', 'dd']
               
        self.assertEqual(expected, actual)  

                
if __name__ == '__main__':
    unittest.main(exit=False)
