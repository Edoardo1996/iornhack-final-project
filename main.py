from utils import cleaning, config

def main():
    # Load data
    data_raw = cleaning.load_data(config.DB_PATH)
    print(data_raw.head())

if __name__ == '__main__':
    main()