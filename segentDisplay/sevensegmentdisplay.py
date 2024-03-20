class SevenSegmentDisplay:

    def print_number(self, number):
        def display_zero():
            print("""
                            #####
                            #   #
                            #   #
                            #   #
                            #####

                            """)
            return "11111101"

        def display_one():
            print("""
                                #
                                #
                                #
                                #
                                #

                            """)
            return "01100001"

        def display_two():
            print("""
                            #####
                                #
                            #####
                            #
                            #####

                            """)
            return "11011011"

        def display_three():
            print("""
                            #####
                                #
                            #####
                                #
                            #####

                            """)
            return "11110011"

        def display_four():
            print("""
                            #   #
                            #   #
                            #####
                                #
                                #

                            """)
            return "01100111"

        def display_five():
            print("""
                            #####
                            #
                            #####
                                #
                            #####

                            """)
            return "10110111"

        def display_six():
            print("""
                            #####
                            #
                            #####
                            #   #
                            #####

                            """)
            return "10111111"

        def display_seven():
            print("""
                            #####
                                #
                                #
                                #
                                #

                            """)
            return "11100001"

        def display_eight():
            print("""
                            #####
                            #   #
                            #####
                            #   #
                            #####

                            """)
            return "11111111"

        def display_nine():
            print("""
                            #####
                            #   #
                            #####
                                #
                            #####

                            """)
            return "11100111"

        display_functions = {
            "11111101": display_zero,
            "01100001": display_one,
            "11011011": display_two,
            "11110011": display_three,
            "01100111": display_four,
            "10110111": display_five,
            "10111111": display_six,
            "11100001": display_seven,
            "11111111": display_eight,
            "11100111": display_nine
        }

        if number in display_functions:
            return display_functions[number]()
        else:
            print("Invalid number")


display = SevenSegmentDisplay()
display.print_number("11100111")
