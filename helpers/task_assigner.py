def assign_debugging_tasks(df):
    tasks = {}
    pairs = df.groupby('pair')
    for pair, group in pairs:
        group = group.reset_index()
        for i in range(len(group)):
            person = group.iloc[i]
            partner = group.iloc[(i + 1) % len(group)]
            tasks[person['name']] = f"Check homework of {partner['name']}"
    return tasks
