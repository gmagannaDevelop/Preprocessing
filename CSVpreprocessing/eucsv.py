
import sys
import os

def main():
    usage_msg = """
        eucsv : Take a csv file and reformat it.

        usage :
            $ python3 eucsv <file_name.csv>

        Expected output : 
                $ cat <file_name.csv>
                    price;tag;stock
                    3,5;hello;4
                    5,5;hallo;50

                $ cat <file_name_comma.csv>
                    price,tag,stock
                    3.5,hello,4
                    5.5,hallo,50
    """

    if len(sys.argv) != 2:
        print(usage_msg)
        sys.exit()
    else:
        in_file  = sys.argv[1]
        out_file = in_file.replace('.', '_comma.')

    with open(in_file, 'r') as I, open(out_file, 'w') as O:
        for line in I:
            O.write( 
                    line.replace(',', '.').replace(';', ',')
                   )


    # Check if file was successfully created:
    if os.path.split(in_file)[0]:
        if out_file in os.listdir(os.path.split(in_file)[0]):
            return True
        else:
            return False
    else:
        if out_file in os.listdir('.'):
            return True
        else:
            return False

if __name__ == '__main__':
    main()

