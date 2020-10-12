# Read in data set
# df = pd.read_csv("data/data_set.csv")
# print(df)
# print(df['FG'].size)

# roster = mean_player(df)
# print(roster)
# net_change_table = generate_net_change_table(roster, df)

# z_score_dict = generate_z_score_dict(net_change_table)
# for stat in z_score_dict:
#     print(stat + ": ", end='')
#     print(z_score_dict[stat])

# print(net_change_table)
# z_score_table = generate_z_score_table(net_change_table)
# print_top_n(z_score_table, "Z_AVG", 10)
# print(z_score_table)

# roster = draft_player('Stephen Curry', roster, df)

# print(roster)
# net_change_table = generate_net_change_table(roster, df)
# print(net_change_table)
# z_score_table = generate_z_score_table(net_change_table)
# print(z_score_table)
# print(find_player('Kyrie Irving', z_score_table))
# print_top_n(z_score_table, "Z_AVG", 10)

# for column in z_score_table:
#     print(column)
#     print(z_score_table[column].min())
#     print(z_score_table[column].max())
