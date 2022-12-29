#!/usr/bin/env python3
import ipdb

class Book:
    pass

    def __init__( self, title ):
        self.title = title.title()

    def get_page_count( self ):
        return self._page_count

    def set_page_count( self, page_count ):
        if type( page_count ) is int and page_count > 0 :
            self._page_count = page_count
        else: print( "page_count must be an integer" )

    def turn_page( self ):
        print( "Flipping the page...wow, you read fast!" )

    page_count = property( get_page_count, set_page_count, )

# ipdb.set_trace()