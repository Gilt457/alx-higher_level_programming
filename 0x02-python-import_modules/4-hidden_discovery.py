#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module"""
    import hidden_4

    concealed_names = dir(hidden_4)
    for concealed_name in concealed_names:
        if concealed_name[:2] != "__":
            print(concealed_name)

