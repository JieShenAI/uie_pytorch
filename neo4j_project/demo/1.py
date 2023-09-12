import neo4j
from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "jieshenai"))


# print(driver)
def example(driver: neo4j.Driver) -> int:
    """Call all young people "My dear" and get their count."""
    record = driver.execute_query(

    )
    assert record is not None  # for typechecking and illustration
    count = record[0]
    assert isinstance(count, int)
    return count


cnt = example(driver)
print(cnt)

driver.close()  # close the driver object
