import luigi
import subprocess

class DockerBuild(luigi.Task):
    """Brings up the environment and runs tests via Docker Compose."""
    
    def output(self):
        return luigi.LocalTarget("pipeline_success.marker")

    def run(self):
        print("--- SRE Action: Orchestrating Docker Compose ---")
        try:
            subprocess.run([
                "docker", "compose", "up", "--build", 
                "--exit-code-from", "test_app", "--abort-on-container-exit"
            ], check=True)
            
            # create the final marker
            with self.output().open('w') as f:
                f.write("Full pipeline (Build + Test) passed in Docker.")
                
        finally:
            # SRE Standard: Always clean up, even on failure
            print("--- Cleaning up containers ---")
            subprocess.run(["docker", "compose", "down"], check=True)

if __name__ == '__main__':
    # We only need to trigger the final task
    luigi.run()
