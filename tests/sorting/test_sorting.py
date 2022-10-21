from src.sorting import sort_by


def test_sort_by_criteria():
    about_jobs = [
        {"min_salary": 2000, "max_salary": 40000, "date_posted": "2022-01-11"},
        {"min_salary": 3000, "max_salary": 50000, "date_posted": "2021-10-31"},
        {"min_salary": 5000, "max_salary": 70000, "date_posted": "2022-04-01"},
    ]
    results = {
        "min_salary": 2000,
        "max_salary": 70000,
        "date_posted": "2022-04-01",
    }

    for criteria in results.keys():
        sort_by(about_jobs, criteria)
        assert about_jobs[0][criteria] == results[criteria]
