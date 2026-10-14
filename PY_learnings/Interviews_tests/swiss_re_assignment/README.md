# Claims ETL Pipeline

This PySpark job reads the claim and policyholder CSV files, applies the
specified transformations, calls Hashify for each distinct claim ID, and
writes the required `processed_claims.csv` file.

## Run

From the repository root:

```powershell
python -m pip install -r requirements.txt
python .\src\claim_etl_job.py `
  --claims-input .\input_data\claim_data.csv `
  --policyholders-input .\input_data\policyholder_data.csv `
  --output .\output\processed_claims.csv
```

The output is a headered CSV with these columns, in order:

```text
claim_id,policyholder_name,region,claim_type,claim_priority,claim_amount,claim_period,source_system_id,hash_id
```

Run the tests with:

```powershell
python -m pytest .\tests -q
```

## Assumptions

- `claim_type` is derived from the `claim_id` prefix; the similarly named
  input field in the sample claims file is ignored.
- Unknown prefixes produce `Unknown`.
- Missing policyholder matches remain null because the join is left-sided.
- Invalid or missing dates produce `Unknown` for `claim_period`.
- Hashify requests run once per distinct non-null claim ID. The API response's
  `Digest` field is written to `hash_id`.
- The driver performs the external requests before joining the hash lookup to
  the distributed claims DataFrame. This avoids a row-level Spark UDF for the
  small sample workload.

For production-scale data, move Hashify calls to a rate-limited batch process
or an approved internal hashing service. The current design intentionally
keeps the external dependency isolated from Spark worker execution.

On Windows, local Spark may require `winutils.exe` and `hadoop.dll` in
`.hadoop\bin`; the job detects that workspace-local directory automatically.
