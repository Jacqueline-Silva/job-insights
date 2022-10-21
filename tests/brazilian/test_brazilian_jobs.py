from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    verify_keys_incorrects = ["titulo", "salario", "tipo"]
    verify_keys_corrects = ["title", "salary", "type"]
    list_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in list_jobs:
        for key_correct in verify_keys_corrects:
            assert key_correct in job

        for key_incorrect in verify_keys_incorrects:
            assert key_incorrect not in job
