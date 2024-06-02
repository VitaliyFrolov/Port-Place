import { ApplicationForm } from '@/entities/ApplicationForm';
import { Container } from '@/shared/ui/Container';
import { Title } from '@/shared/ui/Title';
import styles from './ResidentsBlock.module.scss';

export const ResidentsBlock = () => {
    return (
        <Container>
            <section className={styles.residents}>
                <Title
                    tag="h2"
                    size='l'
                    className={styles.residents__title}
                >
                    Резиденты
                </Title>
                <div className={styles.residents__content}>
                    <p>
                        Команда Port Place состоит из молодых <br />
                        и амбициозных предпринимателей <br />
                        предоставляющих различные товары и услуги. <br />
                    </p>
                    <ApplicationForm />
                </div>
            </section>
        </Container>
    )
};