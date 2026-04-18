class SORTracker {
    set<pair<int, string>> s;
    set<pair<int, string>>::iterator cur;

public:
    SORTracker() {
        s.emplace(0, ""); // 哨兵
        cur = s.begin();
    }

    void add(string name, int score) {
        pair<int, string> p = {-score, name};
        s.emplace(p);
        if (p < *cur) --cur;
    }

    string get() {
        return cur++->second;
    }
};

