import wget


def clean_caption(input_text, fillers):

    input_text = str(input_text)
    input_text = input_text.split(" ")

    output_text = ''

    for j in range(0, len(input_text), 1):

        i = input_text[j]

        if i == 'arafed' or i == 'araffe':
            if j+1 < len(input_text):
                if input_text[j+1][0:1].lower() in ['a', 'e', 'i', 'o', 'u']:
                    output_text = output_text + 'an'
                else:
                    output_text = output_text + 'a'

        elif i not in fillers:
            output_text = output_text + i[0:1].upper() + i[1:]

        else:
            output_text = output_text + i

        output_text = output_text + " "

    output_text = output_text[0:1].upper() + output_text[1:]

    return output_text


def download_model():
    wget.download(
        'https://drive.google.com/uc?export=view&id=1KJ50-zxUqiJlmdQLikBLpp3wa-a33bTR')
    wget.download(
        'https://drive.google.com/uc?export=view&id=1bkZ8NvrPaWnrHE93AtLpbBqqm78vwu_l')
