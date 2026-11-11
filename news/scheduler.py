from operator import imod

from apscheduler.schedulers.background import BackgroundScheduler
import feedparser
from .models import News, NewsSource, Category
from datetime import datetime
import time


def update_rss_feeds():
    categories = Category.objects.all()
    new_count = 0
    for category in categories:
        sources = NewsSource.objects.filter(category=category)

        for source in sources:
            if source.is_active:
                try:
                    feed = feedparser.parse(source.rss_url)
                except Exception as e:
                    print(f"خطا در خواندن {source.rss_url}: {e}")
                    continue
            else:
                continue
            #
            # for s in source.items.all():
            #     s.delete()


            for entry in feed.entries:
                obj, created = News.objects.get_or_create(
                    link=entry.link,

                    defaults={
                        'source': source,
                        'title': entry.title,
                        'summary': entry.get('summary', ''),
                        'published':datetime.fromtimestamp(time.mktime(entry.published_parsed)),
                        'category': category,
                    }

                )
                if created:
                    new_count += 1

    print(f"✅ {new_count} خبر جدید اضافه شد")


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        update_rss_feeds,
        'interval',
        hours=2,
        # minutes=30,
        # seconds=5,
        id='update_rss_feeds_job',
        replace_existing=True,
    )
    scheduler.start()