class MovieRentingSystem:
    def __init__(self, _, entries: List[List[int]]):
        self.shop_movie_to_price = {}  # (shop, movie) -> price
        self.unrented_movie_to_price_shop = defaultdict(SortedList)  # movie -> [(price, shop)]
        self.rented_movies = SortedList()  # [(price, shop, movie)]

        for shop, movie, price in entries:
            self.shop_movie_to_price[(shop, movie)] = price
            self.unrented_movie_to_price_shop[movie].add((price, shop))

    # 获取 unrented_movie_to_price_shop[movie] 的前 5 个 shop
    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.unrented_movie_to_price_shop[movie][:5]]

    # 借电影
    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[(shop, movie)]
        # 从 unrented_movie_to_price_shop 移到 rented_movies
        self.unrented_movie_to_price_shop[movie].discard((price, shop))
        self.rented_movies.add((price, shop, movie))

    # 还电影
    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[(shop, movie)]
        # 从 rented_movies 移到 unrented_movie_to_price_shop
        self.rented_movies.discard((price, shop, movie))
        self.unrented_movie_to_price_shop[movie].add((price, shop))

    # 获取 rented_movies 的前 5 个 shop 和 movie
    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented_movies[:5]]

