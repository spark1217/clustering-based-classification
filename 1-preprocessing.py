import pandas as pd

# load data
goods_info = 'data/data-trans/Goods Info May 27.csv'
ec_info = 'data/data-trans/EcInfo conversion.csv'
ticket_info = 'data/data-trans/Ticket Info May 27.csv'
user_info = 'data/data-trans/User Info May 27.csv'

goods_df_copy = pd.read_csv(goods_info, low_memory=False)
ec_df_copy = pd.read_csv(ec_info, low_memory=False)
ticket_df_copy = pd.read_csv(ticket_info, low_memory=False)
user_df_copy = pd.read_csv(user_info, low_memory=False)


# drop all columns that all values are null
def drop_null_columns(df):
    drop_all_nans = df.dropna(axis=1, how='all')
    return drop_all_nans



goods_df_copy = drop_null_columns(goods_df_copy)
ec_df_copy = drop_null_columns(ec_df_copy)
ticket_df_copy = drop_null_columns(ticket_df_copy)
user_df_copy = drop_null_columns(user_df_copy)

goods_df_copy = goods_df_copy[['date','time','category','merchandise','quantity','Total sales','Payment ID','Payment/refund','Customer ID','Customer reference ID']]
ec_df_copy = ec_df_copy[['order_date','order_id','product_id','quantity','total_amount','fc_member_id','bid','purchase_season','status','fc_status','gender','birth','grade_cd']]
ticket_df_copy = ticket_df_copy[['ticket_id','event_id','event_date','order_id','order_date','outlet','quantity','price_code','price_level','price','is_cancel','bid','fc_member_id','status','fc_status','season_id','grade_cd','gender','birth','reception_class']]
user_df_copy = user_df_copy[['fc_member_id','season_id','bid','grade_cd','status','reception_class','apply_datetime','apply_class','price','admission_class','gender','birth']]

goods_df_copy.to_csv('data/data-trans/processed_goods.csv', index=False)
ec_df_copy.to_csv('data/data-trans/processed_ec.csv', index=False)
ticket_df_copy.to_csv('data/data-trans/processed_ticket.csv', index=False)
user_df_copy.to_csv('data/data-trans/processed_user.csv', index=False)
