import { Container } from '@/shared/ui/Container';
import { Title } from '@/shared/ui/Title';
import styles from './AboutBlock.module.scss';

export const AboutBlock = () => {
    return (
        <Container>
            <section className={styles.about}>
                <Title
                    tag='h2'
                    size='l'
                    className={styles.about__title}
                >
                    О нас
                </Title>
                <div className={styles.about__content}>
                    <p>
                        Пространство Port Place - креативное пространство, <br />
                        где каждый модет найти что-то для себя. <br />
                        На первом этаже распологается зона ритейла <br />
                        предоставляющая услуги наших резидентов. <br />
                        На втором этаже расположена игровая зона с <br />
                        бильярдными стомами и настольным теннисом <br />
                    </p>
                    <div className={styles.about__image}>
                        3D
                    </div>
                </div>
            </section>
        </Container>
    )
};