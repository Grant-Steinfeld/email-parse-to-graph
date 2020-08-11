def write_file( path, fileName, content):
    full_path_ = "{}/{}".format(path, fileName)
    print("writing to ", full_path_)
    with open(full_path_, 'w') as f:
        f.write(content)
