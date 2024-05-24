import { FC } from 'react';
import { List } from '@/shared/ui/List';
import styles from './Ticker.module.scss';

interface TickerPrpos {
    data: any[];
};

export const Ticker: FC<TickerPrpos> = (props) => {
    const {
        data,
    } = props;

    const templateLine = (item: any) => (
        <div className={styles.line}>
            {item.title}
        </div>
    );

    return (
        <section className={styles.line__wrapper}>
            <List
                isLoading={false}
                data={data}
                template={templateLine}
                className={styles.line__list}
            />
        </section>
    )
};