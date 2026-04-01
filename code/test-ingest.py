from impala.dbapi import connect
import os


#host=ccycloud-1.cml-pvc-ocp.root.comops.site (HS2_SERVER Load Balancer - hiveserver2_load_balancer from config)
#port=10015 (HS2_SERVER port - hiveserver2_load_balancer from config)
#auth_mechanism=GSSAPI (leave this as is)
#use_http_transport=True (leave this as true)
#http_path="cliservice" (leave this as is)
#use_ssl=True (if hive.server2.use.SSL from config is checked, this is true, otherwise false)
#kerberos_service_name=hive (kerberos_princ_name from config)

conn = connect(
            host="ccycloud-1.cml-pvc-ocp.root.comops.site",
            port=10015,
            auth_mechanism="GSSAPI",
            use_http_transport=True,
            http_path="cliservice",
            use_ssl=True,
            kerberos_service_name = "hive",
        )








conn = connect(
            host="ccycloud-1.nightly-cm-tj.root.comops.site",
            port=10015,
            auth_mechanism="GSSAPI",
            use_http_transport=True,
            http_path="cliservice",
            use_ssl=True,
            kerberos_service_name = "hive",
        )
df2 = pd.read_sql("SELECT * FROM default.your_table LIMIT 10", hive_conn)
print(df2)