height_inp = float(input('enter the height of your wall: '))
width_inp = float(input('enter the width of your wall: '))
coverage_inp = 5
buckets_of_paint = 0
def paint_needed_func(height, width, coverage):
    global bucket_or_buckets
    bucket_or_buckets = 0
    if ((height * width) / coverage) > 1:
        bucket_or_buckets = 'buckets'
    elif ((height * width) / coverage) < 0.5:
        bucket_or_buckets = '(a small bucket)'
    else:
        bucket_or_buckets = 'bucket'
    print(f'you need {round((height * width) / coverage)} {bucket_or_buckets} of paint')

paint_needed_func(height = height_inp, width = width_inp, coverage = coverage_inp)
