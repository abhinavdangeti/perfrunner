from perfrunner.tests import PerfTest
from perfrunner.helpers.cbmonitor import with_stats


class KVTest(PerfTest):

    @with_stats()
    def access(self):
        super(KVTest, self).timer()

    def run(self):
        self.load()
        self.wait_for_persistence()

        self.hot_load()
        self.wait_for_persistence()
        self.compact_bucket()

        self.workload = self.test_config.get_access_settings()
        self.access_bg()
        self.access()
        self.shutdown_event.set()


class LatencyTest(KVTest):

    @with_stats(latency=True)
    def access(self):
        super(LatencyTest, self).timer()

    def run(self):
        super(LatencyTest, self).run()
        for operation in ('get', 'set'):
            for percentile in (0.9, 0.95, 0.99):
                self.reporter.post_to_sf(
                    *self.metric_helper.calc_kv_latency(operation=operation,
                                                        percentile=percentile)
            )


class BgFetcherTest(KVTest):

    def run(self):
        super(BgFetcherTest, self).run()
        self.reporter.post_to_sf(self.metric_helper.calc_avg_ep_bg_fetched())


class FlusherTest(KVTest):

    def run(self):
        super(FlusherTest, self).run()
        self.reporter.post_to_sf(self.metric_helper.calc_avg_drain_rate())
