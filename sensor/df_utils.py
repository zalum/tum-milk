def log_df(df, logger, comment):
    logger.info("================== {} =================".format(comment))
    print(df.info())
    if len(df.columns)>0:
        print(df.describe())
    print(df)
    logger.info("================== {} ================= end.".format(comment))
    return df


def flatten_columns(df):
    df.columns = list(map(lambda x: x.replace("_sum", ""), ["_".join(col) for col in df.columns]))
    return df


def excelize(df, excel_writer, sheet_name):
    if not df.empty:
        df.to_excel(excel_writer, sheet_name=sheet_name)
    return df
