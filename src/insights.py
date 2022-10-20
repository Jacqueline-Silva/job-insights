from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them"""
    list_jobs = read(path)
    list_unique_job_types = {row["job_type"] for row in list_jobs}
    return list_unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type"""
    list_job_type = [job for job in jobs if job["job_type"] == job_type]
    return list_job_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them"""
    list_jobs = read(path)
    list_unique_industries = {
        row["industry"] for row in list_jobs if row["industry"] != ""
    }
    return list_unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry"""
    list_by_industry = [job for job in jobs if job["industry"] == industry]
    return list_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs"""
    list_jobs = read(path)
    salaries = [
        int(row["max_salary"])
        for row in list_jobs
        if row["max_salary"].isdigit()
    ]
    max_salary = max(salaries)
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs"""
    list_jobs = read(path)
    salaries = [
        int(row["min_salary"])
        for row in list_jobs
        if row["min_salary"].isdigit()
    ]
    max_salary = min(salaries)
    return max_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job"""
    verify_keys = "max_salary" in job and "min_salary" in job

    if not verify_keys:
        raise ValueError()
    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError()

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
