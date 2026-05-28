import asyncio
from app.database import AsyncSessionLocal
from app.models.base import InspectionJob

async def test():
    async with AsyncSessionLocal() as db:
        job = InspectionJob(
            id='test-123',
            company_id='1',
            created_by='1',
            job_ref='TEST-001',
            client_name='Test',
            product_name='Test',
            master_file_path='/tmp/test',
            scan_file_path='/tmp/test',
            input_source='multi_up',
            status='queued'
        )
        db.add(job)
        await db.commit()
        print('Success')

asyncio.run(test())